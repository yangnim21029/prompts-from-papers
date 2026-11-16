# 醫療 AI 評估：依臨床量表評閱答案

PrecepTron 的模板把病例、題目、待評答案與評分規準組成請求，輸出結構化分數。六個任務映射與配套量表都保留。論文報告的一致性提升主要來自微調，使用同一 prompt 並不等於使用同一評分模型。

論文為 *Scaling Clinical Judgment to Evaluate Medical AI*。

作者：Thomas A. Buckley、Zahir Kanjee、Peter G. Brodeur、Byron Crowe、Anthony M. Pettinato、Aashna P. Shah、Adrian D. Haimovich、Liam G. McCoy、Daniel Restrepo、Jason A. Freed、Ethan Goh、Jonathan H. Chen、Laura Zwaan、Katherine E. Goodman、Daniel J. Morgan、Raja-Elie E. Abdulnour、Adam Rodman、Arjun K. Manrai。

研究機構：哈佛醫學院、史丹佛大學、MIT、BIDMC、University of Alberta、Erasmus MC、University of Maryland等。首次提交：2026-09-11；本頁依據 arXiv:2609.12822v2。

## 研究怎麼做，結果如何

研究以 Qwen3-32B 為基礎，使用 LoRA 在每任務 2–46 個病例上微調。GRAND-ROUNDS 整體含七項既有研究、六類任務與 9,217 筆評分；11 位評分醫師評閱 160 位臨床醫師及九個 AI 模型的答案。主要模型比較涵蓋五類臨床任務，對照未微調 Qwen3-32B、前沿模型及醫師間一致性。160 位是答案撰寫者，不是評分醫師人數。

五類任務中，PrecepTron相對原始模型的醫師評分一致性提高4–15個百分點；例如NEJM CPC由82%升至92%；可重現五項既有研究的主要結果而不新增人工評分。

優勢主要來自模型微調，單靠few-shot或GEPA提示最佳化未穩定重現；不是診斷輔助或患者結局試驗；不同任務仍有落差，例如一項任務低於Gemini。

## 公開材料與使用方式

官方程式、模板與量表依 MIT 保存，固定於查核當日 commit。論文採 arXiv non-exclusive distribution license，PDF 僅提供來源。

用研究案例、待評答案與相應標準答案／測試計畫填入占位符。management_reasoning 需使用 upstream/rubrics/management.json 的該題 rubric；其餘量表已完整嵌入 system。bi_triage 是上游沿用 CPC Bond 模板的映射。

和對應任務提示一起使用；保留逐題評分點數、參考答案與例外，不以摘要取代。

## 原始 prompt 與配套材料

### 1. management_reasoning

需要提供：case_vignette；question_text；response；rubric。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

Example output:
{
  "score": 3,
  "justification": "The response demonstrates..."
}
```

**User prompt**

```text
## Case Vignette
{case_vignette}

## Question
{question_text}

## Response to Score
{response}

## Scoring Rubric
{rubric}
```

原檔：`prompts/management_reasoning.md`。來源定位：`preceptron/prompts.py: SYSTEM_PROMPT lines 21–33; MANAGEMENT_REASONING lines 180–191`。

### 2. diagnostic_reasoning

需要提供：case_vignette；final_diagnosis；question_text；response。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
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

Total maximum: 19 points
```

**User prompt**

```text
## Final Diagnosis
{final_diagnosis}

## Case Vignette
{case_vignette}

## Question
{question_text}

## Response to Score
{response}
```

原檔：`prompts/diagnostic_reasoning.md`。來源定位：`preceptron/prompts.py: _DIAGNOSTIC_REASONING_SYSTEM lines 41–80; _DIAGNOSTIC_REASONING_USER lines 193–204`。

### 3. r_idea

需要提供：question_text；response。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
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
- 2: >= 2 objective data points in explanation of at least one alternative diagnosis
```

**User prompt**

```text
## Question
{question_text}

## Response to Score
{response}
```

原檔：`prompts/r_idea.md`。來源定位：`preceptron/prompts.py: _R_IDEA_SYSTEM lines 83–121; _R_IDEA_USER lines 206–211`。

### 4. cpc_bond

需要提供：final_diagnosis；response。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
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
- 5: the actual diagnosis was suggested in the differential
```

**User prompt**

```text
## Final Diagnosis
{final_diagnosis}

## Response to Score
{response}
```

原檔：`prompts/cpc_bond.md`。來源定位：`preceptron/prompts.py: _CPC_BOND_SYSTEM lines 123–138; _CPC_BOND_USER lines 213–218`。

### 5. cpc_management

需要提供：response；test_plan。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
You are an expert clinical evaluator. You will be given a clinical response and a scoring rubric.
Score the response according to the rubric. You must output ONLY valid JSON with your scoring result.

Your output must be a JSON object with these fields:
- "score": the numeric score you assign
- "justification": a brief explanation of your scoring decision

## Testing Plan Rubric

- 0: The LLM testing plan would be unhelpful
- 1: The LLM testing plan would have been helpful or yielded the diagnosis via another test not used in the actual case
- 2: The LLM-suggested testing plan was nearly identical to the actual testing plan
```

**User prompt**

```text
## Reference Test Plan
{test_plan}

## Response to Score
{response}
```

原檔：`prompts/cpc_management.md`。來源定位：`preceptron/prompts.py: _CPC_MANAGEMENT_SYSTEM lines 140–152; _CPC_MANAGEMENT_USER lines 220–225`。

### 6. bi_triage

需要提供：final_diagnosis；response。

用途：臨床研究答案評分。原文範圍：system＋user 全文；未刪減量表或 JSON 規格。

**System prompt**

```text
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
- 5: the actual diagnosis was suggested in the differential
```

**User prompt**

```text
## Final Diagnosis
{final_diagnosis}

## Response to Score
{response}
```

原檔：`prompts/bi_triage.md`。來源定位：`preceptron/prompts.py: _CPC_BOND_SYSTEM lines 123–138; _CPC_BOND_USER lines 213–218`。

### 7. bond scoring rubric

用途：必要評分量表／題目規則。原文範圍：官方 JSON 全檔。

```json
{
  "name": "Bond Score",
  "description": "The scale does not contain a score of 1.",
  "max_score": 5,
  "possible_scores": [0, 2, 3, 4, 5],
  "scoring": [
    {"score": 0, "text": "no suggestions close to the target diagnosis"},
    {"score": 2, "text": "the suggestions included something related, but unlikely to be helpful"},
    {"score": 3, "text": "the suggestions included something closely related that might have been helpful"},
    {"score": 4, "text": "the suggestions included something very close, but not exact"},
    {"score": 5, "text": "the actual diagnosis was suggested in the differential"}
  ]
}
```

原檔：`upstream/rubrics/bond.json`。來源定位：`rubrics/bond.json`。

### 8. diagnostic scoring rubric

用途：必要評分量表／題目規則。原文範圍：官方 JSON 全檔。

```json
{
  "questions": {
    "q1": {"question_text": "Diagnosis #1", "max_score": 1, "possible_scores": [0, 1]},
    "q2": {"question_text": "Diagnosis #2", "max_score": 1, "possible_scores": [0, 1]},
    "q3": {"question_text": "Diagnosis #3", "max_score": 1, "possible_scores": [0, 1]},
    "q4": {"question_text": "Supporting Factors #1", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q5": {"question_text": "Supporting Factors #2", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q6": {"question_text": "Supporting Factors #3", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q7": {"question_text": "Opposing Factors #1", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q8": {"question_text": "Opposing Factors #2", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q9": {"question_text": "Opposing Factors #3", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q10": {"question_text": "Final diagnostic decision", "max_score": 2, "possible_scores": [0, 1, 2]},
    "q11": {"question_text": "Three additional steps", "max_score": 2, "possible_scores": [0, 1, 2]}
  },
  "case_diagnoses": {
    "1": "Cholesterol Embolization Syndrome",
    "2": "Paraneoplastic Dermatomyositis",
    "3": "Infective Endocarditis",
    "4": "Multiple Myeloma",
    "5": "Pernicious Anemia",
    "6": "Polycythemia Vera"
  }
}
```

原檔：`upstream/rubrics/diagnostic.json`。來源定位：`rubrics/diagnostic.json`。

### 9. management scoring rubric

用途：必要評分量表／題目規則。原文範圍：官方 JSON 全檔。

```json
{
  "case_1": {
    "q1": {
      "question_text": "Based on the information you have at this time, what is the differential diagnosis for this incidental lung nodule?",
      "max_score": 6,
      "rubric_items": [
        {"points": 1, "text": "Primary lung malignancy"},
        {"points": 1, "text": "Metastasis to the lung"},
        {"points": 1, "text": "Tuberculosis"},
        {"points": 1, "text": "Non-TB primary lung infection"},
        {"points": 1, "text": "Rheum/auto-immune condition"},
        {"points": 1, "text": "Benign tumor/granuloma/calcification"}
      ]
    },
    "q2": {
      "question_text": "What additional information (from patient or medical record) could you non-invasively obtain that would help further hone the differential diagnosis for this lung nodule?",
      "max_score": 9,
      "rubric_items": [
        {"points": 1, "text": "Smoking history (ex. pack years)"},
        {"points": 1, "text": "Environmental exposure history"},
        {"points": 1, "text": "Cancer history (personal or family)"},
        {"points": 1, "text": "Prior history of lung infections"},
        {"points": 1, "text": "Prior TB testing, treatment, or BCG vaccination"},
        {
          "points": 2,
          "text": "Two of three of the following:",
          "required_count": 2,
          "subitems": [
            "Spiculation of nodule",
            "Solid or subsolid nodule",
            "Upper lobe location of nodule"
          ]
        },
        {
          "points": 1,
          "text": "One of two of the following:",
          "required_count": 1,
          "subitems": [
            "History of rheum/auto-immune disease (personal or family)",
            "Geography of current/previous living"
          ]
        },
        {
          "points": 1,
          "text": "One of two of the following:",
          "required_count": 1,
          "subitems": ["Hemoptysis", "Lymphadenopathy"]
        }
      ]
    },
    "q3": {
      "question_text": "This patient is being planned for discharge today and is expecting to leave today to go to rehab. What factors would influence your decision on keeping the patient in the hospital or deferring to the outpatient setting for additional work up?",
      "max_score": 11,
      "rubric_items": [
        {"points": 1, "text": "Patient's understanding of current condition"},
        {"points": 1, "text": "Patient's understanding of importance of follow-up"},
        {"points": 1, "text": "Patient's ability to navigate the healthcare system"},
        {"points": 1, "text": "Family/caregiver support"},
        {"points": 1, "text": "Quality/effectiveness of health system operations for patients with lung nodules"},
        {"points": 1, "text": "Risk/cost of additional time in the hospital"},
        {"points": 1, "text": "Plan for anticoagulation"},
        {"points": 1, "text": "Biopsy plan in place"},
        {
          "points": 1,
          "text": "One of two of the following:",
          "required_count": 1,
          "subitems": ["Risk tolerance of patient", "Risk tolerance of clinician"]
        },
        {
          "points": 2,
          "text": "Two of four of the following:",
          "required_count": 2,
          "subitems": [
            "PCP/outpatient care access",
            "Location/distance of rehab or ease of communication with outpatient rehab",
            "Availability/ability to attend outpatient specialist appointments while at outpatient rehab",
            "Timeliness of outpatient specialty appointments"
          ]
        }
      ]
    },
    "q4": {
      "question_text": "If you were to defer the workup to the outpatient setting, what would be your process?",
      "max_score": 7,
      "rubric_items": [
        {"points": 1, "text": "Ensure patient/family understanding of current condition"},
        {"points": 1, "text": "Emphasize importance of follow-up given concern for malignancy"},
        {"points": 1, "text": "Referral for outpatient biopsy/scheduled prior to discharge"},
        {"points": 1, "text": "Assess patient/family needs in terms of discharge"},
        {"points": 1, "text": "Communication of discharge recommendation to outpatient care team"},
        {"points": 1, "text": "Clear communication of plan/anticipatory guidance to patient/family in appropriate language"},
        {"points": 1, "text": "Establish an anticoagulation plan (ex. hold, continue, discontinue)"}
      ]
    },
    "q5": {
      "question_text": "If you were to keep the patient in the hospital for additional investigations, at what point in those investigations would you discharge the patient?",
      "max_score": 3,
      "rubric_items": [
        {"points": 1, "text": "After biopsy"},
        {"points": 1, "text": "After resumption of oral anticoagulation"},
        {"points": 1, "text": "After clear delineation of outpatient care plan"}
      ]
    }
  },
  "case_2": {
    "q1": {
      "question_text": "How long would you anticoagulate in this case before you biopsy the liver lesion?",
      "max_score": 5,
      "scoring_note": "5 points for either option",
      "acceptable_answers": [
        "4 weeks as long as no DVT on recheck at 4 weeks",
        "4-6 weeks"
      ]
    },
    "q1b": {
      "question_text": "What is your rationale for choosing that amount of time?",
      "max_score": 12,
      "scoring_note": "IF they gave a SHORT response (<3 months), give two points each for up to six of the SHORT items (total of 12). If they gave a long response (> 3 months), give two points each for the LONG items, up to 8.",
      "sections": [
        {
          "label": "SHORT",
          "condition": "If participant chose SHORT duration (<3 months)",
          "scoring_note": "IF they gave a SHORT response (<3 months), give two points each for up to six of these (total of 12)",
          "points_per_item": 2,
          "max_points": 12,
          "items": [
            "50% of people will have clot resolution at 4 weeks of anticoagulation",
            "Anticoagulation pause for procedure will be short and patient will resume anticoagulation soon afterwards",
            "Even if this is a solid cancer and therefore not necessarily curable, it may still improve outcome by treating the cancer early (so early diagnosis is important)",
            "Most VTE will have improved by 4-6 weeks (even if not always fully resolved)",
            "Even after only 6 weeks of total anticoagulation, the majority of patients do well (despite the high risk of recurrence with so short an anticoagulation duration)",
            "There is a risk the malignancy will progress if we don't biopsy promptly",
            "There is a risk the malignancy will have complications if we don't biopsy promptly",
            "The mass could be a curable condition, e.g. lymphoma, and so prompt biopsy is important"
          ]
        },
        {
          "label": "LONG",
          "condition": "If participant chose LONG duration (>3 months)",
          "scoring_note": "If they gave a long response (> 3 months), give two points each for these, up to 8",
          "points_per_item": 2,
          "max_points": 8,
          "items": [
            "Data exist showing 6 months anticoagulation has lower recurrence than if only treated for 6 weeks",
            "There is an especially high risk of clot recurrence in cancer-associated clot (as compared to non-cancer-associated clot)",
            "This is unlikely to be curable condition (i.e., likely a metastatic disease) and so less urgency to diagnose and treat the mass",
            "Patient has a heavy clot burden [distinct from heavily symptomatic]"
          ]
        }
      ]
    },
    "q2": {
      "question_text": "Thinking beyond this specific patient, which general factors would you consider in a decision about timing of biopsy for such a hepatic lesion in a patient with new pulmonary embolism and DVT? Which factors would make you more likely to biopsy PROMPTLY? And which factors would make you more likely to DELAY biopsy after a longer period of anticoagulation?",
      "max_score": 20,
      "scoring_note": "Give 2 points each up to 10 for both PROMPT and DELAY, with a maximum score of 20.",
      "sections": [
        {
          "label": "PROMPT",
          "points_per_item": 2,
          "max_points": 10,
          "items": [
            "There is a need for a biopsy (i.e., you can't just make the diagnosis by imaging)",
            "There is an urgency to defining the lesion to start treatment",
            "The patient has symptoms from the disease/mass",
            "The patient has organ compromise related to/from the presumed mass (e.g. biliary obstruction, tumor lysis syndrome, etc)",
            "The venous thromboembolism is limited to lower extremities or is a small volume PE (i.e. lower risk clot)",
            "There is concern for a potentially curable condition, e.g. lymphoma",
            "There is concern for a rapidly progressive cancer, e.g. lymphoma, which could increase the risk of complications if treatment delayed",
            "There has been rapid progression of the disease/mass already",
            "A DVT or PE is asymptomatic",
            "The DVT is present in upper rather than lower extremities",
            "Clot is distal lower extremity DVT rather than proximal lower extremity DVT"
          ]
        },
        {
          "label": "DELAY",
          "points_per_item": 2,
          "max_points": 10,
          "items": [
            "If radiology had a lower suspicion for malignancy/suspicion for some other non-malignant condition",
            "If there was a way to make the diagnosis without having to biopsy anything",
            "There is hemodynamically substantial pulmonary embolism",
            "There is a large clot burden",
            "There is poor cardiopulmonary reserve",
            "There is concern for a slow-growing (rather than fast-growing) malignancy",
            "There is concern for metastatic non-curable disease rather than a curable condition like lymphoma (which is less likely to be helped by a difference in a few weeks of therapy because therapies are non-curative and less relatively efficacious)",
            "There is concern for metastatic disease rather than a curable condition like lymphoma (and there is an increased risk for VTE recurrence with short rather than long periods of anticoagulation in people with high burden of cancer compared to people with low burden of cancer)",
            "The patient has recurrent clots",
            "The patient has recurrent clots, especially in setting of prior anticoagulation holds",
            "The duration of a necessary periprocedural anticoagulation hold is longer (as opposed to shorter)",
            "The patient could not tolerate chemotherapy if found to have a cancer"
          ]
        }
      ]
    },
    "q3a": {
      "question_text": "When a patient on a direct oral anticoagulant is to undergo an invasive procedure like a liver biopsy, how long before the procedure would you hold anticoagulation?",
      "max_score": 5,
      "scoring_note": "5 points for either answer",
      "acceptable_answers": [
        "48 hours",
        "48 hours (unless chronic kidney disease or using dabigatran, then possibly 72 hours)"
      ]
    },
    "q3b": {
      "question_text": "What is your rationale for choosing that amount of time?",
      "max_score": 6,
      "scoring_note": "2 for each, up to 6 points total",
      "points_per_item": 2,
      "max_items_credited": 3,
      "rubric_items": [
        {"points": 2, "text": "PAUSE trial showing this is safe"},
        {"points": 2, "text": "ACCP guidelines"},
        {"points": 2, "text": "ACC/AHA Afib guidelines"},
        {"points": 2, "text": "Pharmacokinetic data"},
        {"points": 2, "text": "The liver is a non-compressible site"},
        {"points": 2, "text": "Liver bleeding has a high risk of catastrophic bleeding"}
      ]
    },
    "q4": {
      "question_text": "When a patient on a direct oral anticoagulant is to undergo an invasive procedure like a liver biopsy, what factors would help you decide whether or not to use an agent for bridging anticoagulation?",
      "max_score": 10,
      "scoring_note": "Give 2 points for each, up to 10 points in total",
      "points_per_item": 2,
      "max_items_credited": 5,
      "rubric_items": [
        {"points": 2, "text": "The indication for anticoagulation"},
        {"points": 2, "text": "The presence or absence of a high-risk hereditary or acquired thrombophilia (e.g. antiphospholipid syndrome, protein C/S deficiency, anti-thrombin 3 deficiency, etc)"},
        {"points": 2, "text": "Whether patient has had recurrent thrombosis"},
        {"points": 2, "text": "Whether patient has had recurrent thrombosis, especially during prior anticoagulation holds"},
        {"points": 2, "text": "Whether the clot is recent or not"},
        {"points": 2, "text": "The CHADS2-VaSC score (exclusively in patients with Afib)"},
        {"points": 2, "text": "The duration of anticoagulation already for the current VTE"},
        {"points": 2, "text": "The provoked/unprovoked nature of the VTE"},
        {"points": 2, "text": "The procedural bleeding risk"},
        {"points": 2, "text": "The compressibility of the procedure site"},
        {"points": 2, "text": "The danger of bleeding at that particular biopsy site"},
        {"points": 2, "text": "The presence/suspicion for malignancy (since higher risk for clotting off anticoagulation)"}
      ]
    },
    "q5": {
      "question_text": "Would you recommend placement of an IVC filter in this case? Why or why not?",
      "max_score": 6,
      "scoring_note": "Max score is 6 (this would be any combination of yes (ie 4 points for yes reasons for yes, and 2 points no reasons for no). ONLY GET POINTS IF THEY CITE YES REASONS FOR YES AND NO REASONS FOR NO. Give 2 points for each reason cited.",
      "sections": [
        {
          "label": "WHY YES",
          "scoring_note": "2 points for each, up to 6 points total. Only award if respondent also cites WHY NO reasons.",
          "points_per_item": 2,
          "items": [
            "This person needs a biopsy",
            "This person needs a pause of anticoagulation and can't safely pause anticoagulation",
            "There are no prospective data answering the exact question but the balance of benefits and harms suggest benefit in a scenario like this",
            "The patient had a large hemodynamically significant PE recently",
            "Recurrent clot would be dangerous"
          ]
        },
        {
          "label": "WHY NO",
          "scoring_note": "Only award if respondent also cites WHY YES reasons.",
          "points_per_item": 2,
          "items": [
            "There is no hard indication in this case based on the existing data",
            "Data are limited and have only compared anticoagulation alone versus anticoagulation plus filter",
            "Data are absent for guidance around IVC use and anticoagulation pauses",
            "An anticoagulation pause is short (and therefore feasible in this case)",
            "The patient is extremely thrombogenic already, and the IVC filter increases thrombogenic risk",
            "There are risks of IVC filter placement",
            "There are risks of IVC filter retrieval"
          ]
        }
      ]
    },
    "q6": {
      "question_text": "What are the arguments for and against doing an IVC filter in general?",
      "max_score": 16,
      "scoring_note": "Give the sum of the scores in your answer (max 16). 2 points each, up to 6 total for FOR; 2 points each, up to 10 total for AGAINST.",
      "sections": [
        {
          "label": "FOR",
          "scoring_note": "2 points each, up to 6 total",
          "points_per_item": 2,
          "max_points": 6,
          "items": [
            "IVC filters could prevent some morbidity from VTE when anticoagulation is impossible/contraindicated",
            "IVC filters could prevent some morbidity from VTE when anticoagulation needs to be paused",
            "IVC filters could prevent some morbidity from VTE when anticoagulation is impossible/contraindicated in patients with poor cardiopulmonary reserve",
            "IVC filters could prevent some morbidity from VTE when anticoagulation needs to be paused in patients with poor cardiopulmonary reserve",
            "There is probably a reduction in PE",
            "There is a low procedural risk in the short term for placement of an IVC",
            "Compared to many years ago, IVC filters placed are now more consistently subsequently retrieved"
          ]
        },
        {
          "label": "AGAINST",
          "scoring_note": "2 points each, up to 10 total",
          "points_per_item": 2,
          "max_points": 10,
          "items": [
            "IVC filters are prothrombotic",
            "A patient can still get PEs from clots that form on the IVC filter",
            "IVC filters are often left in for too long",
            "IVC filters are often left in for too long and then as a result are difficult to retrieve",
            "There is a lack of data relevant to situations we see in clinical practice (e.g. while patients are not able to be on anticoagulation)",
            "IVC filters do not reduce VTE overall",
            "Outside of those with poor cardiopulmonary reserve, there is no mortality benefit for IVC filters",
            "There is a low rate of retrieval of IVC filters",
            "There are poor systems to ensure retrieval of IVC filters",
            "There are adverse effects/procedural risks from the IVC filter placement procedure"
          ]
        }
      ]
    }
  },
  "case_3": {
    "q1": {
      "question_text": "In this patient, would you perform a paracentesis and a thoracentesis? What factors push you in one way or another?",
      "max_score": 4,
      "rubric_items": [
        {"points": 1, "text": "Answered yes to paracentesis"},
        {"points": 1, "text": "Answered yes to thoracentesis"},
        {
          "points": 2,
          "text": "Two of the three of the following:",
          "required_count": 2,
          "subitems": [
            "The patient has shortness of breath",
            "The patient has abdominal discomfort",
            "There is a low likelihood to improve with diuretics"
          ]
        }
      ]
    },
    "q2": {
      "question_text": "Would you provide any blood products to this patient, either before or after a procedure? Why or why not?",
      "max_score": 4,
      "rubric_items": [
        {"points": 1, "text": "Answered no for blood products"},
        {
          "points": 1,
          "text": "One of the two of the following:",
          "required_count": 1,
          "subitems": [
            "FFP does not reduce risk of bleeding",
            "Platelets do not reduce risk of bleeding"
          ]
        },
        {
          "points": 2,
          "text": "Two of the three of the following:",
          "required_count": 2,
          "subitems": [
            "Blood products cause harm with volume overload",
            "Blood products cause harm with portal hypertension",
            "Blood products cause harm with transfusion reaction"
          ]
        }
      ]
    },
    "q3": {
      "question_text": "What are the possible risks and benefits of giving FFP in this patient?",
      "max_score": 4,
      "rubric_items": [
        {"points": 1, "text": "There are no benefits in giving FFP"},
        {
          "points": 3,
          "text": "Three of the five of the following:",
          "required_count": 3,
          "subitems": [
            "Portal hypertension",
            "Transfusion reaction",
            "Transfusion-related infection",
            "Transfusion-associated lung injury (TRALI)",
            "Waste of blood products"
          ]
        }
      ]
    },
    "q4": {
      "question_text": "After her ICU admission, you call her radiologist to ask that he stop giving FFP. How would you approach that conversation?",
      "max_score": 4,
      "rubric_items": [
        {
          "points": 4,
          "text": "Four of the seven of the following:",
          "required_count": 4,
          "subitems": [
            "Assume positive intent",
            "Thank proceduralist",
            "Ask him why he is doing it",
            "Explain the facts of the case",
            "Request that they stop",
            "Explain negative outcome",
            "Consideration of the medium of conversation (e-mail versus phone)"
          ]
        }
      ]
    },
    "q5": {
      "question_text": "Should a PleurX catheter be placed to aid in drainage of her pleural effusion? What are the risks and benefits?",
      "max_score": 4,
      "rubric_items": [
        {
          "points": 1,
          "text": "One of the two of the following factors recognizing the contingencies pointing to yes:",
          "required_count": 1,
          "subitems": ["If truly diuretic refractory", "If not a candidate for TIPS"]
        },
        {
          "points": 2,
          "text": "Two of three of the following benefits:",
          "required_count": 2,
          "subitems": [
            "Reduces number of procedures",
            "Smaller amount drained more frequently",
            "Can be done at home"
          ]
        },
        {"points": 1, "text": "Increases the likelihood of infection (risk)"}
      ]
    },
    "q6": {
      "question_text": "Should a Transjugular Intrahepatic Portosystemic Shunt (TIPS) be considered? What are the risks and benefits?",
      "max_score": 4,
      "rubric_items": [
        {"points": 1, "text": "Yes, a TIPS should be considered."},
        {"points": 1, "text": "Risk of liver failure with an elevated MELD"},
        {"points": 1, "text": "Risk of hepatic encephalopathy"},
        {
          "points": 1,
          "text": "One of the following two benefits:",
          "required_count": 1,
          "subitems": ["Improved nutrition", "Improved frailty status"]
        }
      ]
    },
    "q7": {
      "question_text": "What are possible reasons for the adjustment in her needs for paracentesis?",
      "max_score": 3,
      "rubric_items": [
        {
          "points": 3,
          "text": "Three of the five of the following:",
          "required_count": 3,
          "subitems": [
            "Reduction in total volume of blood products",
            "Changed alcohol intake",
            "Improved adherence to diuretics",
            "Improved nutrition",
            "Less salt in diet"
          ]
        }
      ]
    }
  },
  "case_4": {
    "q1": {
      "question_text": "In addition to continuing telemetry monitoring, would you recommend any additional monitoring, testing, or treatment at this time? If so, what?",
      "max_score": 4,
      "rubric_items": [
        {"points": 1, "text": "Prophylactic anticoagulation to prevent VTE/DVT (e.g. enoxaparin 40mg daily) \u2013 Credit for either correct labeling of the intervention, or correct med + dose combination"},
        {"points": 1, "text": "TSH"},
        {
          "points": 2,
          "text": "Inclusion of up to 2 of the following:",
          "scoring_note": "1 point each, max 2",
          "required_count": 2,
          "points_per_item": 1,
          "subitems": [
            "Echocardiogram",
            "Electrolyte assessment and/or repletion",
            "Evaluation for additional triggers (e.g. pain, constipation, etc....)"
          ]
        }
      ]
    },
    "q2a": {
      "question_text": "Would you recommend to this patient that she be started on therapeutic anticoagulation?",
      "max_score": 2,
      "rubric_items": [
        {"points": 2, "text": "Yes, start therapeutic anticoagulation"}
      ]
    },
    "q2b": {
      "question_text": "What factors would influence your decision?",
      "max_score": 7,
      "rubric_items": [
        {"points": 2, "text": "Patient preference and/or risk tolerance"},
        {"points": 2, "text": "CHA2DS2-VaSc or CHADS2 score"},
        {"points": 1, "text": "Listing only 1-2 component of these scoring systems separately, without mentioning the score itself"},
        {
          "points": 3,
          "text": "Inclusion of up to 3 of the following 5 factors:",
          "scoring_note": "1 point for each, max 3",
          "required_count": 3,
          "points_per_item": 1,
          "subitems": [
            "HAS-BLED score",
            "Duration of a-fib episodes",
            "# of post-op episodes",
            "Information potentially obtained from an echo",
            "A-fib burden (i.e. % of time spent in a-fib)"
          ]
        }
      ]
    },
    "q3": {
      "question_text": "If the decision was made to start the patient on therapeutic anticoagulation on hospital day #4 (i.e. immediately after the asymptomatic, 2 hour long episode of a-fib), what would be the best choice for anticoagulation?",
      "max_score": 3,
      "rubric_items": [
        {"points": 3, "text": "Apixaban, rivaroxaban, edoxaban, dabigatran, therapeutic enoxaparin"},
        {"points": 1, "text": "Unfractionated heparin gtt"}
      ]
    },
    "q4a": {
      "question_text": "The patient is about to be discharged. Would you discharge her with an ambulatory ECG monitor?",
      "max_score": 1,
      "rubric_items": [
        {"points": 1, "text": "Yes"}
      ]
    },
    "q4b": {
      "question_text": "If so, what type of monitor would you choose?",
      "max_score": 1,
      "rubric_items": [
        {"points": 1, "text": "Holter and/or Ziopatch (i.e. \"14 day Holter\")"}
      ]
    },
    "q4c": {
      "question_text": "What factors should be considered in the choice of monitor for this patient?",
      "max_score": 2,
      "rubric_items": [
        {
          "points": 2,
          "text": "Inclusion of up to 2 of the following:",
          "scoring_note": "1 point each, max 2",
          "required_count": 2,
          "points_per_item": 1,
          "subitems": [
            "Cost of monitor",
            "Ease of insurance approval",
            "Duration of monitoring period",
            "Likelihood of the patient experiencing a lethal arrhythmia"
          ]
        }
      ]
    },
    "q4d": {
      "question_text": "What would you do with the information from the monitor?",
      "max_score": 3,
      "rubric_items": [
        {"points": 1, "text": "Determine anticoagulation plan (i.e. whether or not the patient requires anticoagulation, or the duration of anticoagulation)"},
        {
          "points": 2,
          "text": "Inclusion of up to 2 of the following:",
          "scoring_note": "1 point each, max 2",
          "required_count": 2,
          "points_per_item": 1,
          "subitems": [
            "Determine if the patient requires rate control",
            "Determine if the patient requires rhythm control",
            "Determine if the patient requires more diagnostic testing"
          ]
        }
      ]
    }
  },
  "case_5": {
    "q1": {
      "question_text": "How would you evaluate for involuntary weight loss?",
      "max_score": 19,
      "scoring_note": "Each item is worth the specified points. Maximum total is up to 19 points.",
      "rubric_items": [
        {"points": 1, "text": "CBC"},
        {"points": 1, "text": "Metabolic Panel"},
        {"points": 1, "text": "UA/Urine Culture"},
        {"points": 1, "text": "CT Chest"},
        {"points": 1, "text": "CT Abdomen/Pelvis"},
        {"points": 1, "text": "Cancer Biomarkers"},
        {"points": 0.5, "text": "A1C"},
        {"points": 0.5, "text": "Cortisol Testing"},
        {"points": 1, "text": "TSH"},
        {"points": 1, "text": "TB Evaluation"},
        {"points": 1, "text": "HIV Testing"},
        {"points": 1, "text": "HCV Testing"},
        {"points": 1, "text": "Autoimmune Serologic Testing"},
        {"points": 0.5, "text": "EGD"},
        {"points": 0.5, "text": "Colonoscopy"},
        {"points": 0.5, "text": "Pap Smear"},
        {"points": 0.5, "text": "Mammogram"},
        {"points": 1, "text": "Examining Dentition"},
        {"points": 1, "text": "Evaluating for Dysphagia"},
        {"points": 1, "text": "Screening for food insecurity"},
        {"points": 1, "text": "Screening for depression"},
        {"points": 1, "text": "Screening for dementia"}
      ]
    },
    "q2": {
      "question_text": "What is your approach to evaluating her fevers?",
      "max_score": 14,
      "scoring_note": "1 point per item unless noted. Maximum total is up to 14 points.",
      "rubric_items": [
        {"points": 1, "text": "Repeat Blood Cultures"},
        {"points": 1, "text": "Repeat Paracentesis"},
        {"points": 1, "text": "UA/Urine Culture"},
        {"points": 1, "text": "Respiratory Viral Panel"},
        {"points": 1, "text": "Sputum Cultures (also acceptable: tracheal aspirate, respiratory culture, Bronch/BAL, max 1 point)"},
        {"points": 1, "text": "LP"},
        {"points": 1, "text": "Fungal Cultures"},
        {
          "points": 4,
          "text": "Imaging:",
          "scoring_note": "1 point each",
          "points_per_item": 1,
          "subitems": [
            "CT Chest",
            "CT Abdomen/Pelvis",
            "DVT ultrasound",
            "Brain MRI"
          ]
        },
        {"points": 2, "text": "HIV/HCV Testing", "scoring_note": "1 point each"},
        {"points": 1, "text": "Cancer Biomarkers"}
      ]
    },
    "q3": {
      "question_text": "What do you do with her antibiotics and why?",
      "max_score": 10,
      "scoring_note": "Select the single best matching response and assign the corresponding points.",
      "rubric_items": [
        {"points": 10, "text": "Assuming no infectious source is identified after 48-72 hours and the patient is not improving, stop antibiotics (either all at once or sequentially)"},
        {"points": 10, "text": "Assuming no infectious source is identified after 48-72 hours, de-escalate to SBP prophylaxis"},
        {"points": 10, "text": "Assuming no infectious source is identified after 48-72 hours and the patient is not improving, stop vancomycin but continue meropenem"},
        {"points": 5, "text": "Continue empiric treatment with vanc/meropenem for 7 days"},
        {"points": 0, "text": "Assuming no infectious source is identified after 48-72 hours and the patient is not improving, change classes of antibiotics but maintain relatively broad-spectrum coverage"},
        {"points": 0, "text": "Continue empiric treatment with vanc/meropenem and add micafungin (or a similar agent)"}
      ]
    },
    "q4": {
      "question_text": "As the patient is not getting any better after two weeks in the ICU, the family broaches the subject of comfort measures. What factors go into your decision in this patient to make her CMO?",
      "max_score": 12,
      "rubric_items": [
        {"points": 3, "text": "Patient wishes from prior advanced care planning discussions or documents OR preferences of healthcare proxy if patient wishes were unclear"},
        {"points": 2, "text": "Overall family preferences"},
        {"points": 2, "text": "Patient's ESLD/MELD Score"},
        {"points": 2, "text": "Whether the patient is a transplant candidate"},
        {"points": 3, "text": "Likelihood of meaningful functional recovery"}
      ]
    },
    "q5": {
      "question_text": "How do you explain this diagnosis to the family?",
      "max_score": 12,
      "scoring_note": "8 points max if includes both apology and empathy, 4 points if only includes one.",
      "rubric_items": [
        {"points": 8, "text": "Provide an apology AND Express Empathy", "scoring_note": "8 points max if includes both, 4 points if only includes one"},
        {"points": 4, "text": "Discuss the nature of drug-induced neurotoxicity, Point out how drug-induced neurotoxicity is relatively rare (and this likely led to a delay in diagnosis), Discuss that drug-induced neurotoxicity is presumed but not confirmed, Discussion that ESLD and/or renal dysfunction can increase the likelihood of drug toxicities", "scoring_note": "4 points if any of these points included"}
      ]
    }
  }
}
```

原檔：`upstream/rubrics/management.json`。來源定位：`rubrics/management.json`。

### 10. r_idea scoring rubric

用途：必要評分量表／題目規則。原文範圍：官方 JSON 全檔。

```json
{
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
        {"score": 4, "text": "4 features present"}
      ]
    },
    "D": {
      "name": "Differential Diagnosis",
      "description": "Offers more than one relevant diagnostic possibility, committing to what is most likely and considering what is less likely or unlikely yet important to consider for the main chief complaint. If the chief complaint is a diagnosis or syndrome then differential to rate may be around the differential for that exacerbation.",
      "max_score": 2,
      "possible_scores": [0, 1, 2],
      "scoring": [
        {"score": 0, "text": "No differential"},
        {"score": 1, "text": "Differential is implicitly stated, given as a diagnostic category (e.g, cardiac), OR implicitly prioritized"},
        {"score": 2, "text": "Differential is explicitly stated AND explicitly prioritized"}
      ]
    },
    "E": {
      "name": "Explanation of Lead Diagnosis",
      "description": "Explains the reasoning behind the lead diagnosis, including the epidemiology and key features and how these compare with the patient's presentation. If objective data points are not clearly linked to the lead diagnosis or alternative diagnosis, then only designate points to lead OR alternative diagnosis and NOT both.",
      "max_score": 2,
      "possible_scores": [0, 1, 2],
      "scoring": [
        {"score": 0, "text": "No explanation"},
        {"score": 1, "text": "1 objective data point in explanation of the lead diagnosis"},
        {"score": 2, "text": ">= 2 objective data points in explanation of lead diagnosis"}
      ]
    },
    "A": {
      "name": "Alternative Diagnosis Explained",
      "description": "Explains the reasoning behind alternative diagnoses, including the epidemiology and key features and how these compare with the patient's presentation. If objective data points are not clearly linked to the lead diagnosis or alternative diagnosis, then only designate points to lead OR alternative diagnosis and NOT both.",
      "max_score": 2,
      "possible_scores": [0, 1, 2],
      "scoring": [
        {"score": 0, "text": "No explanation for any alternative diagnosis"},
        {"score": 1, "text": "1 objective data point in explanation of at least one alternative diagnosis"},
        {"score": 2, "text": ">= 2 objective data points in explanation of at least one alternative diagnosis"}
      ]
    }
  }
}
```

原檔：`upstream/rubrics/r_idea.json`。來源定位：`rubrics/r_idea.json`。

### 11. testing_plan scoring rubric

用途：必要評分量表／題目規則。原文範圍：官方 JSON 全檔。

```json
{
  "name": "Testing Plan",
  "max_score": 2,
  "possible_scores": [0, 1, 2],
  "scoring": [
    {"score": 0, "text": "The LLM testing plan would be unhelpful"},
    {"score": 1, "text": "The LLM testing plan would have been helpful or yielded the diagnosis via another test not used in the actual case"},
    {"score": 2, "text": "The LLM-suggested testing plan was nearly identical to the actual testing plan"}
  ]
}
```

原檔：`upstream/rubrics/testing_plan.json`。來源定位：`rubrics/testing_plan.json`。

## 來源與授權

論文授權：arXiv non-exclusive distribution license。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[arXiv 論文](https://arxiv.org/abs/2609.12822v2) · [官方程式固定版本](https://github.com/2v/PrecepTron/tree/4cb33ff861bad729122ce12db7d927bc27ab1b8a) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
