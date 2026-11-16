"""Preset rubrics for tasks with a fixed scoring scheme."""

BOND_SCORE = {
    "name": "Bond Score",
    "description": "The scale does not contain a score of 1.",
    "max_score": 5,
    "possible_scores": [0, 2, 3, 4, 5],
    "scoring": [
        {"score": 0, "text": "no suggestions close to the target diagnosis"},
        {"score": 2, "text": "the suggestions included something related, but unlikely to be helpful"},
        {"score": 3, "text": "the suggestions included something closely related that might have been helpful"},
        {"score": 4, "text": "the suggestions included something very close, but not exact"},
        {"score": 5, "text": "the actual diagnosis was suggested in the differential"},
    ],
}

TESTING_PLAN = {
    "name": "Testing Plan",
    "max_score": 2,
    "possible_scores": [0, 1, 2],
    "scoring": [
        {"score": 2, "text": "Excellent: The predicted testing plan either includes all or most of the tests that were actually performed, or suggests additional relevant tests that would also help reach the correct diagnosis"},
        {"score": 1, "text": "Good: The predicted testing plan differs from what was actually done, but would still provide clinically useful information toward the correct diagnosis"},
        {"score": 0, "text": "Poor: The predicted testing plan would not contribute meaningfully to reaching the correct diagnosis"},
    ],
}

R_IDEA = {
    "name": "R-IDEA",
    "max_score": 10,
    "components": {
        "I": {
            "name": "Interpretive Summary",
            "description": "Provides a concise summary statement that uses semantic vocabulary to highlight the most important elements from history, exam, and testing and to interpret and represent the patient's main problem(s). The presence or absence of the following features is assessed: a) Key risk factors, b) Chief complaint, c) Illness time course, d) Use of semantic qualifiers",
            "max_score": 4,
            "possible_scores": [0, 1, 2, 3, 4],
            "scoring": [
                {"score": 0, "text": "No features present"},
                {"score": 1, "text": "1 feature present"},
                {"score": 2, "text": "2 features present"},
                {"score": 3, "text": "3 features present"},
                {"score": 4, "text": "4 features present"},
            ],
        },
        "D": {
            "name": "Differential Diagnosis",
            "description": "Offers more than one relevant diagnostic possibility, committing to what is most likely and considering what is less likely or unlikely yet important to consider for the main chief complaint.",
            "max_score": 2,
            "possible_scores": [0, 1, 2],
            "scoring": [
                {"score": 0, "text": "No differential"},
                {"score": 1, "text": "Differential is implicitly stated, given as a diagnostic category (e.g, cardiac), OR implicitly prioritized"},
                {"score": 2, "text": "Differential is explicitly stated AND explicitly prioritized"},
            ],
        },
        "E": {
            "name": "Explanation of Lead Diagnosis",
            "description": "Explains the reasoning behind the lead diagnosis, including the epidemiology and key features and how these compare with the patient's presentation.",
            "max_score": 2,
            "possible_scores": [0, 1, 2],
            "scoring": [
                {"score": 0, "text": "No explanation"},
                {"score": 1, "text": "1 objective data point in explanation of the lead diagnosis"},
                {"score": 2, "text": ">= 2 objective data points in explanation of lead diagnosis"},
            ],
        },
        "A": {
            "name": "Alternative Diagnosis Explained",
            "description": "Explains the reasoning behind alternative diagnoses, including the epidemiology and key features and how these compare with the patient's presentation.",
            "max_score": 2,
            "possible_scores": [0, 1, 2],
            "scoring": [
                {"score": 0, "text": "No explanation for any alternative diagnosis"},
                {"score": 1, "text": "1 objective data point in explanation of at least one alternative diagnosis"},
                {"score": 2, "text": ">= 2 objective data points in explanation of at least one alternative diagnosis"},
            ],
        },
    },
}

DEFAULT_RUBRICS: dict[str, dict] = {
    "cpc_bond": BOND_SCORE,
    "cpc_management": TESTING_PLAN,
    "r_idea": R_IDEA,
}
