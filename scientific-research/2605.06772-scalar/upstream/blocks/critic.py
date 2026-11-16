import json
import re

import langroid as lr
import langroid.language_models as lm


class Critic:
    """
    Evaluates actor responses and provides feedback + a numerical score
    and explicitly flags common error types.
    """

    ERROR_TYPES = [
        "SIGN_ERROR",
        "MISSING_TERM",
        "PRODUCT_RULE_ERROR",
        "CHAIN_RULE_ERROR",
        "BOUNDARY_CONDITION_MISAPPLIED",
        "UNIT_MISMATCH",
        "ALGEBRA_SIMPLIFY_FAIL",
        "LIMIT_ERROR",
        "NORMALIZATION_ERROR",
        "INCOMPLETE_EXPR",
        "TEST_FAIL",
        "TENSOR_INDEX_ERROR",
        "DIMENSIONAL_CONSISTENCY",
        "SYMMETRY_PRESERVATION",
        "COMBINATORIAL_FACTORS",
        "REGULARISATIONAL_CONSISTENCY",
        "MISSING_JUSTIFICATION_NON-TRIVIAL_STEPS",
        "LIMITING_BEHAVIOUR_FAIL",
        "POSITIVITY_AND_REALITY_CONSTRAINTS_VIOLATION",
        "VIOLATION_OF_WARD_IDENTITIES",
    ]

    def __init__(
        self,
        model="groq/llama-3.3-70b-versatile",
        context_length=16384,
        name="Critic",
        temperature=None,
        character_prompt: str = "",
        provider="groq",
        retain_history=True,
    ):
        llm_kwargs = dict(
            chat_model=model,
            chat_context_length=context_length,
            timeout=600,
        )
        if temperature is not None:
            llm_kwargs["temperature"] = float(temperature)

        # Configure LLM based on provider
        if provider == "ollama":
            # For Ollama, use OpenAIGPTConfig with ollama/ prefix
            if not model.startswith("ollama/"):
                model = f"ollama/{model}"
            llm_kwargs["chat_model"] = model
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)
        elif provider == "llama.cpp":
            # For llama.cpp, use OpenAIGPTConfig with llama.cpp/ prefix
            if not model.startswith("llama.cpp/"):
                model = f"llama.cpp/{model}"
            llm_kwargs["chat_model"] = model
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)
        else:
            # Default to Groq (or any OpenAI-compatible provider)
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)

        self.config = lr.ChatAgentConfig(
            llm=llm_config,
            name=name,
        )
        self.agent = lr.ChatAgent(self.config)
        self.character_prompt = character_prompt
        self.retain_history = retain_history
        self.character_prompt_set = False

    def evaluate(self, text: str, turns: int = 1, model_sln: str = ""):
        """
        Returns a dict:
            {
                "feedback": str,
                "score": float,
                "SIGN_ERROR": bool,
                "MISSING_TERM": bool,
                ...
            }
        """

        # Build error flags instruction
        error_flags_str = ", ".join(self.ERROR_TYPES)

        prompt = (
            "You are a critic. Evaluate the reasoning in the following answer.\n"
            f"A model solution may be provided here: {model_sln}.\n"
            f"Check explicitly for these errors: {error_flags_str}, but in the"
            "freeform text ('textual_feedback') you should also note any other"
            "errors you find.\n"
            "Provide:\n"
            "  1. Internal user feedback to monitor your performance, and kept"
            "hidden from the agent. This is mandatory and mustn't be empty."
            "  2. Textual feedback to the student explaining improvements and"
            "errors, stopping at any that are fatal first, suggesting how to"
            "fix. This is mandatory and mustn't be empty.\n"
            "  3. A numerical score from 0 to 10 (higher is better) based on"
            "the number of errors you find, soundness of reasoning, and clarity"
            "of exposition. This is mandatory.\n"
            "  4. Boolean flags for each error type. This is mandatory.\n\n"
            "Respond in strict JSON with keys: 'user_feedback', 'score',"
            " and 'feedback', where feedback is text for the agent you're"
            "assesing, user_feedback is for an observer analysing your"
            "performance, score is the numerical score, and all other keys are"
            "the error types provided. In 'feedback', you must not include the"
            "names of errors you are checking unless they are explicitly"
            "present in the solution. You must state all problems only once."
            "Your feedback must be constructive and guide the agent toward"
            "fixes for any problems you find, without giving them the answer. \n\n"
            f"Agent's answer:\n{text}"
        )

        # Handle character prompt: only add on first call if retaining history
        if self.character_prompt:
            if not self.retain_history:
                # Always add character prompt if not retaining history
                prompt = f"{self.character_prompt}\n\n{prompt}"
            elif not self.character_prompt_set:
                # Add character prompt only on first call if retaining history
                prompt = f"{self.character_prompt}\n\n{prompt}"
                self.character_prompt_set = True
                
        # Clear history if not retaining
        if not self.retain_history:
            self.agent.clear_history()
            
        task = lr.Task(
            self.agent, name=f"{self.config.name}Task", interactive=False
        )
        raw = task.run(prompt, turns=turns)

        # ---- Extract text safely ----
        content = raw.content if hasattr(raw, "content") else str(raw)
        content = content.strip()

        # Remove fenced code blocks if present
        if content.startswith("```"):
            content = re.sub(r"^```[a-zA-Z0-9]*\s*", "", content)
            content = re.sub(r"\s*```$", "", content)

        content = content.strip()

        # ---- Parse JSON safely ----
        try:
            result = json.loads(content)
        except json.JSONDecodeError:
            # Fallback: treat entire content as feedback
            result = {
                "feedback": content,
                "score": None,
            }
            for e in self.ERROR_TYPES:
                result[e] = False

        # ---- Ensure all expected error keys exist ----
        for e in self.ERROR_TYPES:
            result.setdefault(e, False)

        # ---- Group errors into a dedicated sub-dictionary ----
        error_dict = {}
        for e in self.ERROR_TYPES:
            error_dict[e] = bool(result.pop(e, False))

        result["errors"] = error_dict

        return result
