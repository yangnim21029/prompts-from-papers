"""
LLM-judge prompts for each benchmark task.

TASK_SYSTEM_PROMPTS maps each task to a self-contained system prompt with the
rubric baked in. This is the single source of truth for all scoring prompts —
edit here to change what the judge sees for any task.

TASK_USER_PROMPTS maps each task to a user-turn template containing only the
case-specific data (vignette, response, etc.). For management_reasoning the
rubric is still dynamic (one per question), so it remains in the user template
via {rubric}. For the other four tasks the rubric lives in the system prompt.

Both run_benchmark.py and the GEPA experiments import from here.
"""

# ---------------------------------------------------------------------------
# Shared generic system prompt — used only for management_reasoning,
# which has a different rubric per question and passes it dynamically.
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

Example output:
{
  "score": 3,
  "justification": "The response demonstrates..."
}"""


# ---------------------------------------------------------------------------
# Task-specific system prompts — rubric fully baked in.
# Edit these to change how the judge scores each task.
# ---------------------------------------------------------------------------

_DIAGNOSTIC_REASONING_SYSTEM = """\
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

### Part 1 – Structured Reasoning

#### Question 1: Diagnosis — List 3 Possible Diagnoses (0–3 points)
The response should list three possible diagnoses.
- 1 point per diagnosis if it is plausible and appropriate for the case
- 0 points if the diagnosis is implausible or incorrect
Maximum: 3 points

#### Question 2: Support Diagnosis — For each possible diagnosis listed, provide findings/risk factors supporting this hypothesis (0–6 points)
For each diagnosis:
- 2 points: Correct and specific findings or risk factors that support the diagnosis and are grounded in the case
- 1 point: Partially correct or incomplete supporting information
- 0 points: Incorrect, irrelevant, or missing
Maximum: 6 points (2 per diagnosis)

#### Question 3: Opposing Diagnosis — For each possible diagnosis listed, provide findings opposing this hypothesis, or findings that were expected but not present (0–6 points)
For each diagnosis:
- 2 points: Correct identification of findings that contradict the diagnosis or expected findings that are absent
- 1 point: Partially correct or incomplete opposing reasoning
- 0 points: Incorrect, irrelevant, or missing
Maximum: 6 points (2 per diagnosis)

### Part 2 – Final Diagnostic Decision (0–2 points)
- 2 points: Correct diagnosis
- 0 points: Incorrect diagnosis

### Part 3 – Additional Steps (0–2 points)
- 2 points: Appropriate, specific, and clinically useful next steps
- 1 point: Partially appropriate or incomplete
- 0 points: Incorrect or not useful

Total maximum: 19 points"""


_R_IDEA_SYSTEM = """\
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

## R-IDEA Scoring Rubric (Total: 10 points)

### I — Interpretive Summary (0–4 points)
Provides a concise summary statement that uses semantic vocabulary to highlight the most important elements from history, exam, and testing and to interpret and represent the patient's main problem(s). The presence or absence of the following features is assessed: a) Key risk factors, b) Chief complaint, c) Illness time course, d) Use of semantic qualifiers

- 0: No features present
- 1: 1 feature present
- 2: 2 features present
- 3: 3 features present
- 4: 4 features present

### D — Differential Diagnosis (0–2 points)
Offers more than one relevant diagnostic possibility, committing to what is most likely and considering what is less likely or unlikely yet important to consider for the main chief complaint. If the chief complaint is a diagnosis or syndrome then differential to rate may be around the differential for that exacerbation.

- 0: No differential
- 1: Differential is implicitly stated, given as a diagnostic category (e.g, cardiac), OR implicitly prioritized
- 2: Differential is explicitly stated AND explicitly prioritized

### E — Explanation of Lead Diagnosis (0–2 points)
Explains the reasoning behind the lead diagnosis, including the epidemiology and key features and how these compare with the patient's presentation. If objective data points are not clearly linked to the lead diagnosis or alternative diagnosis, then only designate points to lead OR alternative diagnosis and NOT both.

- 0: No explanation
- 1: 1 objective data point in explanation of the lead diagnosis
- 2: >= 2 objective data points in explanation of lead diagnosis

### A — Alternative Diagnosis Explained (0–2 points)
Explains the reasoning behind alternative diagnoses, including the epidemiology and key features and how these compare with the patient's presentation. If objective data points are not clearly linked to the lead diagnosis or alternative diagnosis, then only designate points to lead OR alternative diagnosis and NOT both.

- 0: No explanation for any alternative diagnosis
- 1: 1 objective data point in explanation of at least one alternative diagnosis
- 2: >= 2 objective data points in explanation of at least one alternative diagnosis"""

_CPC_BOND_SYSTEM = """\
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

## Bond Score Rubric
The scale does not contain a score of 1.

- 0: no suggestions close to the target diagnosis
- 2: the suggestions included something related, but unlikely to be helpful
- 3: the suggestions included something closely related that might have been helpful
- 4: the suggestions included something very close, but not exact
- 5: the actual diagnosis was suggested in the differential"""

_CPC_MANAGEMENT_SYSTEM = """\
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

## Testing Plan Rubric

- 0: The LLM testing plan would be unhelpful
- 1: The LLM testing plan would have been helpful or yielded the diagnosis via another test not used in the actual case
- 2: The LLM-suggested testing plan was nearly identical to the actual testing plan"""


TASK_SYSTEM_PROMPTS: dict[str, str] = {
    "management_reasoning": SYSTEM_PROMPT,
    "diagnostic_reasoning": _DIAGNOSTIC_REASONING_SYSTEM,
    "r_idea": _R_IDEA_SYSTEM,
    "cpc_bond": _CPC_BOND_SYSTEM,
    "cpc_management": _CPC_MANAGEMENT_SYSTEM,
    "bi_triage": _CPC_BOND_SYSTEM,
}


def get_system_prompt(task: str) -> str:
    """Return the system prompt for a given task name."""
    if task not in TASK_SYSTEM_PROMPTS:
        raise ValueError(
            f"Unknown benchmark task '{task}'; expected one of {list(TASK_SYSTEM_PROMPTS)}"
        )
    return TASK_SYSTEM_PROMPTS[task]


# ---------------------------------------------------------------------------
# User prompt templates — case-specific data only.
# management_reasoning still passes {rubric} dynamically (varies per question).
# All other tasks have the rubric in the system prompt above.
# ---------------------------------------------------------------------------

MANAGEMENT_REASONING = """\
## Case Vignette
{case_vignette}

## Question
{question_text}

## Response to Score
{response}

## Scoring Rubric
{rubric}"""

_DIAGNOSTIC_REASONING_USER = """\
## Final Diagnosis
{final_diagnosis}

## Case Vignette
{case_vignette}

## Question
{question_text}

## Response to Score
{response}"""

_R_IDEA_USER = """\
## Question
{question_text}

## Response to Score
{response}"""

_CPC_BOND_USER = """\
## Final Diagnosis
{final_diagnosis}

## Response to Score
{response}"""

_CPC_MANAGEMENT_USER = """\
## Reference Test Plan
{test_plan}

## Response to Score
{response}"""


TASK_USER_PROMPTS: dict[str, str] = {
    "management_reasoning": MANAGEMENT_REASONING,
    "diagnostic_reasoning": _DIAGNOSTIC_REASONING_USER,
    "r_idea": _R_IDEA_USER,
    "cpc_bond": _CPC_BOND_USER,
    "cpc_management": _CPC_MANAGEMENT_USER,
    "bi_triage": _CPC_BOND_USER,
}

# Keep for backward compatibility
TASK_PROMPTS = TASK_USER_PROMPTS


def get_prompt(task: str) -> str:
    """Return the user prompt template for a given task name."""
    if task not in TASK_USER_PROMPTS:
        raise ValueError(
            f"Unknown benchmark task '{task}'; expected one of {list(TASK_USER_PROMPTS)}"
        )
    return TASK_USER_PROMPTS[task]
