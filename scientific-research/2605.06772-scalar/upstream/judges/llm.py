from __future__ import annotations

import json
import re
from typing import Any, Dict, Optional

import langroid as lr
import langroid.language_models as lm


def _strip_code_fences(s: str) -> str:
    s = s.strip()
    if s.startswith("```"):
        s = re.sub(r"^```[a-zA-Z0-9]*\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
    return s.strip()


class LLMJudge:
    """
    LLM-based judge: grades whether the actor answer addresses the problem.
    Designed to be compatible with orchestrators that may call judge() with
    different keyword argument names.
    """

    def __init__(
        self,
        model: str = "groq/llama-3.3-70b-versatile",
        context_length: int = 16384,
        name: str = "Judge",
        provider: str = "groq",
        temperature: float = 0.0,
    ):
        # Configure LLM based on provider
        if provider == "ollama":
            # For Ollama, use OpenAIGPTConfig with ollama/ prefix
            if not model.startswith("ollama/"):
                model = f"ollama/{model}"
            llm_config = lm.OpenAIGPTConfig(
                chat_model=model,
                chat_context_length=context_length,
                temperature=float(temperature),
                timeout=600,
            )
        elif provider == "llama.cpp":
            # For llama.cpp, use OpenAIGPTConfig with llama.cpp/ prefix
            if not model.startswith("llama.cpp/"):
                model = f"llama.cpp/{model}"
            llm_config = lm.OpenAIGPTConfig(
                chat_model=model,
                chat_context_length=context_length,
                temperature=float(temperature),
                timeout=600,
            )
        else:
            # Default to Groq (or any OpenAI-compatible provider)
            llm_config = lm.OpenAIGPTConfig(
                chat_model=model,
                chat_context_length=context_length,
                temperature=float(temperature),
                timeout=600,
            )

        self.config = lr.ChatAgentConfig(
            llm=llm_config,
            name=name,
        )
        self.agent = lr.ChatAgent(self.config)

    def judge(
        self,
        actor_answer: Optional[str] = None,
        problem: Optional[dict] = None,
        turns: int = 1,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Accepts flexible call signatures.

        Common orchestrator patterns:
          - judge(actor_output, problem_name=..., turns=...)
          - judge(actor_output=..., problem=..., turns=...)
          - judge(actor_answer=..., problem=..., turns=...)

        We support all by:
          - taking actor_answer explicitly
          - also checking kwargs for actor_output
          - requiring `problem` dict (passed by orchestrator)
        """

        # Back-compat: orchestrator may pass actor_output kwarg
        if actor_answer is None:
            actor_answer = kwargs.get(
                "actor_output") or kwargs.get("answer") or ""

        if problem is None:
            # If your orchestrator doesn't pass problem dict, you must modify it to.
            return {
                "pass": False,
                "score": None,
                "summary": "LLMJudge requires a `problem` dict but none was provided.",
                "missing": ["problem"],
                "major_issues": [
                    "Orchestrator must pass problem dict into LLMJudge.judge()."
                ],
            }

        problem_text = problem.get(
            "initial_prompt") or problem.get("description") or ""

        prompt = (
            "You are a mathematical judge evaluating physics/math solutions using rigorous quantitative criteria.\n"
            "Given: problem statement P, actor solution A, and critic feedback C.\n"
            "Output JSON verdict with mathematically precise scoring based on measurable criteria:\n\n"

            "REQUIRED FIELDS:\n"
            "- pass: boolean where pass = (S_total >= 80) AND (S_correctness >= 40) AND (|E_critical| = 0)\n"
            "- constituent_score_actor: {correctness: S_c, mathematical_rigour: S_r, logical_flow: S_l, quality_of_justification: S_j, completeness: S_m, physical_consistency: S_p}\n"
            "- constituent_score_critic: {accuracy_of_identification: C_a, depth_of_analysis: C_d, constructive_feedback_quality: C_f, technical_understanding: C_t, clarity_of_communication: C_c, comprehensiveness: C_h, pedagogical_value: C_v, objectivity_and_fairness: C_o}\n"
            "- summary_critic: quantitative text evaluation of critic performance with specific metrics\n"
            "- missing_actor: list using taxonomy [UNJUSTIFIED_CLAIMS, INCORRECT_RESULT, INCOMPLETE_DERIVATION, MISSING_BOUNDARY_CONDITIONS, DIMENSIONAL_INCONSISTENCY, CONVERGENCE_FAILURE]\n"
            "- major_issues_actor: list of critical mathematical errors with severity classification\n"
            "- missing_critic: list of critic omissions using error detection taxonomy\n"
            "- actor_critic_progress: bool whether or not you believe the actor"
            "and critic are, or will, make progress in further iterations. You"
            "should err on the side of true if unsure\n"

            "MATHEMATICAL SCORING FUNCTIONS:\n"
            "Total Actor Score: S_total = S_c + S_r + S_l + S_j + S_m + S_p where S_total in [0,100]\n"
            "Total Critic Score: C_total = C_a + C_d + C_f + C_t + C_c + C_h + C_v + C_o where C_total in [0,100]\n\n"

            "ACTOR SCORING RUBRIC (S_total = 100 points):\n"
            "- correctness S_c in [0,50]: Mathematical validity measured by error density rho = N_errors/N_steps\n"
            "  * S_c = 50: rho = 0, all equations mathematically sound, final result within epsilon = 1% of expected\n"
            "  * S_c = 42-49: rho < 0.1, minor computational errors (order 10^-2), method convergent\n"
            "  * S_c = 27-41: 0.1 <= rho < 0.3, some correct intermediate steps, significant logical gaps\n"
            "  * S_c = 0-26: rho >= 0.3, fundamental conceptual errors, non-convergent or divergent approach\n\n"

            "- mathematical_rigour S_r in [0,10]: Formal proof completeness measured by justification ratio J = N_justified/N_statements\n"
            "  * S_r = 10: J = 1.0, all statements have mathematical proof/reference, proper notation throughout\n"
            "  * S_r = 7-9: J >= 0.8, mostly rigorous with minor gaps in intermediate steps\n"
            "  * S_r = 4-6: 0.5 <= J < 0.8, partial justification, some assertions without proof\n"
            "  * S_r = 0-3: J < 0.5, primarily unjustified assertions, informal reasoning dominates\n\n"

            "- logical_flow S_l in [0,10]: Structural coherence measured by dependency graph connectivity\n"
            "  * S_l = 10: Directed acyclic graph (DAG) structure, each step logically follows from previous with clear inference rules\n"
            "  * S_l = 7-9: Mostly sequential progression with minor organizational gaps or circular references\n"
            "  * S_l = 4-6: Some logical dependencies unclear, partial DAG structure with isolated components\n"
            "  * S_l = 0-3: Non-sequential reasoning, multiple logical fallacies, graph has cycles or disconnected components\n\n"

            "- quality_of_justification S_j in [0,10]: Explanation depth measured by reasoning chain length R = avg(explanation_steps_per_result)\n"
            "  * S_j = 10: R >= 3, every mathematical step explained with physical/mathematical principles\n"
            "  * S_j = 7-9: 2 <= R < 3, most steps adequately justified with domain-specific reasoning\n"
            "  * S_j = 4-6: 1 <= R < 2, superficial explanations present but lack depth\n"
            "  * S_j = 0-3: R < 1, minimal explanations, results stated without derivation\n\n"

            "- completeness S_m in [0,10]: Coverage ratio M = N_addressed_requirements/N_total_requirements\n"
            "  * S_m = 10: M = 1.0, all problem components addressed with complete mathematical solutions\n"
            "  * S_m = 7-9: M >= 0.8, most aspects covered with minor omissions in secondary requirements\n"
            "  * S_m = 4-6: 0.5 <= M < 0.8, partial coverage with key elements missing\n"
            "  * S_m = 0-3: M < 0.5, incomplete solution, major problem aspects unaddressed\n\n"

            "- physical_consistency S_p in [0,10]: Domain validity measured by consistency checks\n"
            "  * S_p = 10: All results satisfy dimensional analysis [LMT] consistency, limiting cases behave correctly (t->0, x->infinity), units propagate properly\n"
            "  * S_p = 7-9: Generally consistent with minor dimensional or limiting behavior issues\n"
            "  * S_p = 4-6: Some physical inconsistencies, unit errors in intermediate steps, order-of-magnitude issues\n"
            "  * S_p = 0-3: Unphysical results, dimensional analysis failures, violation of conservation laws\n\n"

            "CRITIC SCORING RUBRIC (C_total = 100 points):\n"
            "- accuracy_of_identification C_a in [0,20]: Error detection measured by precision P = TP/(TP+FP) and recall R = TP/(TP+FN)\n"
            "  * C_a = 18-20: P >= 0.9, R >= 0.9, identifies all significant errors with minimal false positives\n"
            "  * C_a = 14-17: P >= 0.7, R >= 0.7, good error detection with some false positives or missed issues\n"
            "  * C_a = 8-13: 0.5 <= P < 0.7 OR 0.5 <= R < 0.7, moderate error identification capability\n"
            "  * C_a = 0-7: P < 0.5 OR R < 0.5, poor error detection, many false positives or missed critical errors\n\n"

            "- depth_of_analysis C_d in [0,15]: Investigation thoroughness measured by analysis depth D = N_examined_steps/N_total_steps\n"
            "  * C_d = 13-15: D >= 0.8, examines mathematical details, verifies intermediate results, checks alternative approaches\n"
            "  * C_d = 10-12: 0.6 <= D < 0.8, good analysis of main results and most key steps\n"
            "  * C_d = 6-9: 0.4 <= D < 0.6, surface-level examination, misses mathematical subtleties\n"
            "  * C_d = 0-5: D < 0.4, superficial analysis, minimal mathematical investigation\n\n"

            "- constructive_feedback_quality C_f in [0,15]: Improvement guidance measured by actionability A = N_actionable_suggestions/N_total_suggestions\n"
            "  * C_f = 13-15: A >= 0.8, specific mathematical corrections with formulas, references to methods/theorems\n"
            "  * C_f = 10-12: 0.6 <= A < 0.8, good suggestions with some mathematical specificity\n"
            "  * C_f = 6-9: 0.4 <= A < 0.6, general feedback without clear mathematical action items\n"
            "  * C_f = 0-5: A < 0.4, vague suggestions, no specific mathematical guidance\n\n"

            "- technical_understanding C_t in [0,15]: Domain expertise measured by concept accuracy T = N_correct_concepts/N_referenced_concepts\n"
            "  * C_t = 13-15: T >= 0.9, demonstrates deep understanding of relevant physics/math principles with accurate terminology\n"
            "  * C_t = 10-12: 0.7 <= T < 0.9, good grasp of domain concepts with minor inaccuracies\n"
            "  * C_t = 6-9: 0.5 <= T < 0.7, basic understanding with some conceptual gaps or errors\n"
            "  * C_t = 0-5: T < 0.5, limited domain knowledge, multiple conceptual errors\n\n"

            "- clarity_of_communication C_c in [0,10]: Expression effectiveness measured by mathematical language precision\n"
            "  * C_c = 9-10: Uses precise mathematical terminology, unambiguous notation, clear logical structure\n"
            "  * C_c = 7-8: Generally clear with proper mathematical language, minor ambiguities\n"
            "  * C_c = 4-6: Understandable but imprecise mathematical terminology, some unclear expressions\n"
            "  * C_c = 0-3: Imprecise language, mathematical ambiguities, confusing notation\n\n"

            "- comprehensiveness C_h in [0,10]: Coverage completeness measured by aspect coverage H = N_addressed_aspects/N_problem_aspects\n"
            "  * C_h = 9-10: H >= 0.9, addresses all significant mathematical and physical aspects of the solution\n"
            "  * C_h = 7-8: 0.7 <= H < 0.9, covers most important mathematical points\n"
            "  * C_h = 4-6: 0.5 <= H < 0.7, partial coverage of key mathematical issues\n"
            "  * C_h = 0-3: H < 0.5, narrow focus, misses important mathematical aspects\n\n"

            "- pedagogical_value C_v in [0,10]: Learning enhancement measured by educational effectiveness E\n"
            "  * C_v = 9-10: Feedback provides conceptual understanding, method improvement, error prevention strategies\n"
            "  * C_v = 7-8: Some educational value with methodological insights\n"
            "  * C_v = 4-6: Limited learning benefit, focuses on errors without constructive teaching\n"
            "  * C_v = 0-3: Minimal educational value, purely evaluative without learning enhancement\n\n"

            "- objectivity_and_fairness C_o in [0,5]: Bias minimization measured by evaluation consistency\n"
            "  * C_o = 5: Completely evidence-based evaluation using mathematical criteria only\n"
            "  * C_o = 3-4: Mostly objective with minor subjective interpretation of mathematical results\n"
            "  * C_o = 1-2: Some evaluative bias evident in mathematical assessment\n"
            "  * C_o = 0: Clear bias, mathematical evaluation influenced by non-mathematical factors\n\n"

            "QUANTITATIVE PASS CRITERIA:\n"
            "pass = (S_total >= 80) AND (S_correctness >= 40) AND (|E_critical| = 0) AND (rho < 0.1)\n"
            "where E_critical = set of critical mathematical errors, rho = error density\n\n"

            "ERROR TAXONOMY (use specific classifications):\n"
            "- COMPUTATIONAL_ERROR: Arithmetic/algebraic mistakes in calculations\n"
            "- CONCEPTUAL_ERROR: Misunderstanding of fundamental principles\n"
            "- METHODOLOGICAL_ERROR: Incorrect approach or technique selection\n"
            "- DIMENSIONAL_ERROR: Unit/dimension inconsistencies\n"
            "- BOUNDARY_CONDITION_ERROR: Incorrect or missing initial/boundary conditions\n"
            "- CONVERGENCE_ERROR: Non-convergent series, improper limits\n"
            "- APPROXIMATION_ERROR: Invalid approximations or order-of-magnitude errors\n\n"

            "OUTPUT: Strict JSON only (no markdown). Use exact numerical scores based on the mathematical criteria above.\n\n"
            f"PROBLEM:\n{problem_text}\n\n"
            f"ACTOR SOLUTION + CRITIC FEEDBACK:\n{actor_answer}\n"
        )

        task = lr.Task(
            self.agent, name=f"{self.config.name}Task", interactive=False)
        raw = task.run(prompt, turns=turns)
        content = raw.content if hasattr(raw, "content") else str(raw)
        content = _strip_code_fences(content)

        try:
            output = json.loads(content)
            # Ensure required keys exist with defaults
            output.setdefault("constituent_score_actor", {})
            output.setdefault("constituent_score_critic", {})
            output.setdefault("pass", False)
            output.setdefault("summary_critic", "")
            output.setdefault("missing_actor", [])
            output.setdefault("missing_critic", [])
            output.setdefault("major_issues_actor", [])
            output.setdefault("actor_critic_progress", True)

            # Calculate totals
            output["total_score_actor"] = sum(
                output["constituent_score_actor"].values()
            )
            output["total_score_critic"] = sum(
                output["constituent_score_critic"].values()
            )
            return output
        except (json.JSONDecodeError, KeyError, AttributeError, TypeError) as e:
            return {
                "pass": False,
                "constituent_score_actor": {},
                "constituent_score_critic": {},
                "summary_critic": f"Judge returned invalid response: {str(e)}",
                "missing_actor": [],
                "missing_critic": [],
                "major_issues_actor": [content],
                "actor_critic_progress": True,
            }
