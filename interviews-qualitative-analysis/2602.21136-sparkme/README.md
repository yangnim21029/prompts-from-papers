# 半結構式訪談：追蹤訪綱與發現新主題

SparkMe 用模板判斷既定主題是否已充分涵蓋，以及是否值得追問新方向。使用者需提供訪綱、對話紀錄與工具狀態。附錄另有模擬受訪者及三種訪談評估指令。

論文為 *SparkMe: Adaptive Semi-Structured Interviewing for Qualitative Insight Discovery*。

作者：David Anugraha、Vishakh Padmakumar、Diyi Yang。

研究機構：Stanford University（史丹佛大學）。首次提交：2026-02-24；本頁依據 arXiv:2602.21136v1。

## 研究怎麼做，結果如何

研究先以模擬受訪者比較不同 AI 訪談流程，再以來自七種職業的 70 位真人參與者進行使用者研究。系統透過模擬後續對話，衡量預定主題涵蓋、新興主題與訪談回合數之間的取捨。

在模擬受訪者實驗中，作者報告訪綱涵蓋比最佳基準提高 4.7%，並用較少對話回合取得更多新興洞見。真人研究則由參與者與同職業領域的評閱者檢查訪談及洞見；這些結果不能解讀為系統已勝過人類訪談員。

4.7%的量化增益來自模擬受訪者比較；不是優於人類訪談員的證據；重現須多代理規劃流程。

## 公開材料與使用方式

公開核心與評估模板完整保留。訪綱狀態、工具呼叫、模擬與排程需由系統提供。

## 原始 prompt 與配套材料

### 1. 判斷當前主題是否已充分涵蓋

先判斷主題適用事件經驗的 STAR 結構，或屬背景與概念描述；只有涵蓋充分時才彙整筆記並呼叫更新工具。

需要提供：主題清單、目前主題筆記、update_subtopic_coverage 工具。

用途：訪談規劃。原文範圍：全文。

```text
<instructions>

## Process

1. **Determine Subtopic Nature**
   - Infer whether the subtopic is:
  

     * **STAR-appropriate** → if it describes an event, project, or experience involving actions, challenges, or outcomes.
  

     * **Descriptive** → if it focuses on background, motivation, interest, reasoning, or conceptual understanding rather than a specific event.

2. **Evaluate Completeness**
   - For **STAR-appropriate** subtopics:
       * Coverage requires STAR components:
         - **Situation:** Context or background
         - **Task:** Objective or responsibility
         - **Action:** Steps taken or reasoning
         - **Result:** Outcome, metric, or reflection
       * Fully covered when almost all components are clearly present and coherent.
  

       * However, if notes is already comprehensive, feel free to mark it as covered as there are more important subtopics to be covered in later section.
   - For **Descriptive** subtopics:
       * Coverage requires comprehensive factual, reflective, or conceptual detail.
  

       * Fully covered when the main question or theme is explained with sufficient clarity, logic, and completeness (even if not quantifiable).
  

       * However, if notes is already comprehensive, feel free to mark it as covered as there are more important subtopics to be covered in later section.

3. **Aggregation**
  

   - For fully covered subtopics, synthesize the notes into a coherent and concise final summary capturing the essence of what was discussed.
   - Avoid repetition or rephrasing—focus on integration and clarity.

4. **Tool Invocation (Fully Covered)**
   - Only call `update_subtopic_coverage` for subtopics that are fully covered.
   - Each call should include:
       * `subtopic_id`: the ID of the covered subtopic.
       * `aggregated_notes`: the aggregated summary notes.

</instructions>
```

原檔：`prompts/01-subtopic-coverage.en.txt`。來源定位：`A2.p2`。

### 2. 辨認值得追問的新興主題

最多新增一個與既有大題相關、又無法被現有子題涵蓋的新方向。模板提供新穎性、預期資訊增益及直接相關性的判準。

需要提供：topics_list、近期對話、前次摘要與既有事件。

用途：訪談規劃。原文範圍：全文。

```text
<instructions>
## Process
1. Read the topics and subtopics in `topics_list`.
  

2. Read the user’s recent conversation carefully. Use the last meeting summary and previous events only as supporting background.
  

3. Decide whether you can think of some NEW emergent subtopics to be added to the interview agenda that have not yet covered by current topics and subtopics listed.
4. Add exactly one emergent subtopic—the strongest candidate—or none.

## Decision rules (apply strictly)
  

- The idea must fall *within one of the existing topics* and *not related to any existing subtopics*. If it does not clearly map to a parent topic, do NOT add it.
  

- The idea must be *novel*: the idea of emergence topic is RARE, so if it can reasonably be addressed within any existing subtopic (even loosely), do NOT add it.
  

- The idea must enable *new probing that goes beyond deepening existing subtopics*, i.e., it should open up a qualitatively different line of inquiry that could surface emergent insights not reachable by further questioning within current subtopics.
- If multiple candidate ideas appear, select **only the strongest single candidate**.
- If no candidate satisfies all rules, do not add any new subtopic.

## What counts as an emergence
An emergent insight is a type of information that:

  

- Cannot be obtained by asking more detailed or follow-up questions within any existing subtopic.
  

- Reveals a new dimension, pattern, tradeoff, or mental model that reframes how existing subtopics are understood.
  

- Changes how future interview questions would be prioritized, sequenced, or interpreted.
  

- Surfaces higher-order understanding (e.g., cross-cutting constraints, implicit decision criteria, failure modes, or latent strategies).

NOT emergent insights:
- Additional examples, edge cases, or elaborations of existing subtopics.
- Narrow refinements or sub-steps of an existing subtopic.
- Clarifications that improve depth but not scope.
- Rephrasings of existing concepts using different wording.

## Ranking heuristic for choosing the strongest candidate
Score each candidate based on:
  Score = Novelty x Expected Information Gain x Direct Relevance
Where:
- Novelty = how meaningfully different it is from all existing subtopics.
  

- Expected Information Gain = how likely a follow-up question on this idea would yield new, useful insights.
- Direct Relevance = how clearly the idea aligns with its parent topic.

## Practical checks
  

- The emergent subtopic description should be short, clear, and represent an idea (5-10 words, maximum 1 sentence).
- Avoid redundancy, rephrasings, or overly narrow micro-subtopics.
- Do not add subtopics that drift outside the interview’s intended scope.

## Examples
  

- If existing subtopics include "evaluation metrics" and "benchmark selection," and the user mentions "error patterns across languages," treat it as emergent *only if* it cannot reasonably fit under "evaluation."
  

- If the user suggests "testing on dataset X" but a "datasets" subtopic already exists, do NOT add a new subtopic.
</instructions>
```

原檔：`prompts/02-emergent-subtopic.en.txt`。來源定位：`A2.p3`。

### 3. 模擬受訪者的回答與記憶

這組模板供模擬實驗產生受訪者回答，包含資料背景與對話條件；它的角色是受訪者。

需要提供：受訪者背景、聊天紀錄、目前問題與已談內容。

用途：模擬。原文範圍：全文。

```text
RESPOND_TO_QUESTION_PROMPT = """
CONTEXT

PROFILE_BACKGROUND

CHAT_HISTORY

INSTRUCTIONS

OUTPUT_FORMAT
"""

RESPOND_CONTEXT = """
<context>
  

You are playing the role of a real person being interviewed. You are currently in an interview session.

  

You now need to respond: provide a natural response that aligns with your character’s personality and background, as if you are having a genuine conversation with an interviewer.
  

If this is the first turn, you should only say that you are happy to start the interview.
</context>
"""

PROFILE_BACKGROUND_PROMPT = """
This is your background information.
<profile_background>
profile_background
</profile_background>

Here are summaries from your previous interview sessions:
<session_history>
session_history
</session_history>
"""

CHAT_HISTORY = """
  

Here is the conversation history of your interview session so far. You are the <UserAgent>  in the chat history and you need to respond to the interviewer’s last question.
<chat_history>
chat_history
</chat_history>
"""

RESPOND_INSTRUCTIONS_PROMPT = """
<instructions>
# GENERAL INTERVIEW RULES
- Always answer the question asked.
- Never skip a question.
- Do not anticipate follow-up questions.
- Treat this as a real interview: the interviewer controls depth and direction.
- Answer only what is necessary for the current question.

# HUMAN STOPPING HEURISTIC (CRITICAL)
Humans stop talking once they have given a sufficient answer, not a complete one.

- Aim for the first reasonable stopping point.
- Assume the interviewer may interrupt or follow up.
- Do not try to close the topic yourself.

# BREVITY & DEPTH CONTROL (STRICT)
- Answer length: 1-2 sentences.
- Typical answers should reveal approximately one concrete fact or signal.
- Do not compress multiple ideas, timelines, or facts into one answer.

# VAGUE OR OPEN-ENDED QUESTIONS (CRITICAL)
  

If a question is vague, ambiguous, or open-ended to answer without guessing, for example if it sounds like listing some list of topics, then:
- Do NOT invent scope or details.
- Briefly acknowledge the ambiguity (e.g., "I’m not sure which aspect you mean").
  

- Either ask one short clarification question, OR state one reasonable assumption and answer briefly under that assumption.
- Do not do both and do not expand beyond the assumed or clarified scope.

# CONTENT GUIDELINES
- Stay tightly focused on the question’s scope.
- Do not expand across time, roles, or institutions unless asked.
- Do not repeat prior answers unless explicitly prompted.
- Avoid lists unless the interviewer asks for them.
- Avoid meta-commentary about motivation, passion, or energy.

# EMERGENCE (ALLOWED AND ENCOURAGED)
  

You may introduce emergent content that is not explicitly listed in your background, such as:
- Interpretations
- Personal insights
- Opinions
- Non-obvious takeaways

Constraints on emergence:
- Emergent content must be reflective, not biographical.
  

- Do not introduce new life events, credentials, dates, or timeline facts unless asked.
- At most one emergent insight per answer.
- Emergence should add depth, not breadth.

Preferred pattern:
- One profile-grounded anchor
- Optional one emergent insight
- Stop

# STYLE
- Natural, conversational, confident.
- Professional but unscripted.
- Sound like a strong candidate who knows when to stop talking.

# STOPPING RULE (ABSOLUTE)
- End your response immediately after your main point.
- Do not summarize.
  

- Do not add closing remarks such as “happy to elaborate” or “let me know if you’d like more.”
</instructions>
"""

RESPONSE_OUTPUT_FORMAT_PROMPT = """
Respond directly as the user without tags, reasoning, or preamble.

Begin your response now:
"""
```

原檔：`prompts/03-simulated-interviewee.en.txt`。來源定位：`A1.SS5.p2`。

### 4. 評估預定主題涵蓋程度

依參考資料評估訪談是否取得主題所需資訊，作為實驗評分。

需要提供：主題、對話內容與受訪者資料中的參考資訊。

用途：評分。原文範圍：全文。

```text
SYSTEM_PROMPT = """
# Instruction
  

Your task is to evaluate recall accuracy in interview notes. Check whether the **ground truth facts** appear **explicitly** in the interview notes.

Rules:
1. Facts must be stated explicitly (no inference).
2. Components of a fact may be spread across the notes.
3. Extra information does not affect the score.

# Evaluation Rubric

- **5 (Perfect):** All ground truth facts are explicitly found in the interview note.
  

- **4 (Minor Omission):** One minor fact or sub-bullet is missing in the interview note.
- **3 (Partial):** About half of the facts are found in the interview notes.
  

- **2 (Vague Overlap):** General topic mentioned, specifics missing in the interview notes.
- **1 (No Recall):** Ground truth facts are absent in the interview notes.

# Output Format (JSON)
{
    "score": 1-5
}
"""

USER_PROMPT = """
# Input

### Ground Truth Facts
{ground_truth 
### Interview Notes
{all_notes}

### Your Output
"""
```

原檔：`prompts/04-coverage-evaluator.en.txt`。來源定位：`A1.SS6.p2`。

### 5. 辨認及評估新興主題

此組包含新興主題識別及相關評估模板，需保留各模板的輸入脈絡。

需要提供：原訪綱、訪談紀錄、受訪者背景與候選新主題。

用途：評分。原文範圍：全文。

```text
EMERGENT_SUBTOPIC_IDENTIFICATION_TEMPLATE = """
Your task is to identify **Emergent Subtopics** in LLM-led interviews.

  

An emergent subtopic is defined as a **NEW SUBTOPIC** that should be added to the interview agenda.

Emergence is **rare**. Most interviews produce **no new subtopics**.

### Definition of Emergent Subtopic

  

A candidate subtopic qualifies as an emergent subtopic ONLY if it satisfies ALL of the following:

1. It clearly falls **within an existing interview topic**
2. It **does NOT belong to ANY existing subtopic** under that topic
  

   - If it can reasonably be addressed (even loosely) within an existing subtopic, it is NOT emergent
  

3. It enables a **qualitatively new line of inquiry**, not just deeper questioning of an existing subtopic
4. It reveals at least ONE of the following:
   (a) A **new dimension, pattern, or tradeoff** not previously captured
   (b) A **cross-cutting constraint or mental model** that reframes multiple subtopics
  

   (c) A **latent strategy, failure mode, or decision criterion** that would change how the interview is conducted

  

Fluent elaborations, clarifications, examples, or refinements of existing subtopics are **NOT emergent**.

### Ground Truth Facts
<ground_truth_facts>
ground_truth
</ground_truth_facts>

### Interview Notes
<interview_notes>
all_notes
</interview_notes>

### Output Format (STRICT JSON ONLY)
  

If there is no emergent subtopic, simply return EMPTY LIST. Otherwise, provide LIST OF emergent subtopic in the format below:
[
    {
        "emergent_subtopic": "Name or concise description of the emergent subtopic",
        "topic": "Parent interview topic this subtopic belongs to",
  

        "rationale": "Why this subtopic cannot be placed under any existing subtopic and what qualitatively new inquiry it enables"
    }
]

### Your Response
"""

  

EMERGENT_SUBTOPIC_COVERAGE_EVALUATION = """You are a session scribe who assists an interviewer. You observe the dialogue between the interviewer and the candidate, and your role is to determine investigate each subtopic and its notes to determine whether the subtopic has achieved full coverage or not.

Your objectives:
  

1. Identify whether each subtopic should be evaluated using the STAR (Situation, Task, Action, Result) framework or a general descriptive evaluation.
2. Determine whether each subtopic is fully covered.
  

3. Return a final list of covered subtopics with NO duplicates (including semantically duplicated subtopics).

### Process

#### Step 1: Deduplicate Subtopics (MANDATORY)
- Subtopics may appear multiple times in the input.
  

- Treat subtopics with the same or semantically equivalent description as ONE subtopic.
- Create an internal list of UNIQUE subtopics.
- All evaluation must be performed only on this deduplicated list.

#### Step 2: Determine Subtopic Nature
For each UNIQUE subtopic, infer whether it is:
  

- **STAR-appropriate** → describes a specific event, project, or experience involving actions, challenges, or outcomes.
  

- **Descriptive** → focuses on background, motivation, interest, reasoning, or conceptual understanding rather than a specific event.

#### Step 3: Evaluate Completeness
   - For **STAR-appropriate** subtopics:
       * Coverage requires STAR components:
         - **Situation:** Context or background
         - **Task:** Objective or responsibility
         - **Action:** Steps taken or reasoning
         - **Result:** Outcome, metric, or reflection
       * Fully covered when almost all components are clearly present and coherent.
  

       * However, if notes is already comprehensive, feel free to mark it as covered as there are more important subtopics to be covered in later section.
   - For **Descriptive** subtopics:
       * Coverage requires comprehensive factual, reflective, or conceptual detail.
  

       * Fully covered when the main question or theme is explained with sufficient clarity, logic, and completeness (even if not quantifiable).
  

       * However, if notes is already comprehensive, feel free to mark it as covered as there are more important subtopics to be covered in later section.

### Subtopics
<subtopics>
{emergent_subtopics}
</subtopics>

### Interview Notes
<interview_notes>
{all_notes}
</interview_notes>

### Output Format (STRICT JSON ONLY)
Return a LIST of covered subtopics in the following format:

[
  {
    "subtopic_covered": "Unique subtopic name",
    "rationale": "Why this subtopic is covered based on the interview notes"
  }
]

If no subtopic is covered, return:

[]

### Your Response
"""

  

DEDUPLICATION_PROMPT = """You are a post-processing assistant whose ONLY task is to deduplicate covered subtopics.

You are given a LIST of covered subtopics produced by a previous judge.
Some entries may refer to the SAME underlying concept even if phrased differently.

Your goal is to MERGE semantic duplicates and return a CLEAN list of UNIQUE subtopics.

### Definitions

Two subtopics are considered SEMANTIC DUPLICATES if they:
  

- Refer to the same underlying concept, skill, experience, system, or interview question
- Would reasonably be answered by the same explanation
- Differ only in wording, emphasis, or phrasing

Examples:
- "Team leadership experience" = "Leading teams"
- "AI-powered system integration for detecting inconsistencies" =
  "AI as a proactive system integrator for data consistency"

### Deduplication Procedure (MANDATORY)

Follow these steps STRICTLY:

#### Step 1: Identify Duplicate Groups
- Compare all subtopics pairwise.
- Group together subtopics that are semantic duplicates.

#### Step 2: Choose a Canonical Subtopic
For each duplicate group:
- Select ONE canonical subtopic name.
- Prefer:
  - The most concise phrasing
  - The most general formulation (not overly specific unless necessary)
- You MAY rephrase slightly to improve clarity, but do NOT add new meaning.

#### Step 3: Merge Rationales
- Combine evidence from all rationales in the group.
- Remove redundancy.
- Ensure the merged rationale faithfully reflects the interview notes.
- Do NOT introduce new claims.

### Output Rules (STRICT)

- Return ONLY the deduplicated list.
- Each subtopic must appear AT MOST ONCE.
- Do NOT include explanations, commentary, or intermediate steps.
- Output MUST be valid JSON.
- If the input list is empty, return an EMPTY LIST.

### Input Covered Subtopics
<input>
{covered_subtopics}
</input>

### Output Format (STRICT JSON ONLY)

[
  {
    "subtopic_covered": "Canonical subtopic name",
    "rationale": "Merged rationale"
  }
]

### Your Response
"""
```

原檔：`prompts/05-emergence-evaluator.en.txt`。來源定位：`A1.SS6.p3`。

### 6. 評估訪談連貫性與流程

按公開規準判斷訪談的連貫程度與推進方式。

需要提供：完整訪談逐字稿。

用途：評分。原文範圍：全文。

```text
You will be given the full transcript of a semi-structured interview.

  

Evaluate the interviewer’s question-asking behavior across the entire interview using the three dimensions below. Assign one integer score from 1 (very poor) to 5 (excellent) for each dimension as a global, holistic judgment. Do not score individual turns.

Dimension A — Local Coherence Between Consecutive Questions

  

Rate whether successive questions are logically connected to the immediately preceding context.
  

1: Consecutive questions are frequently unrelated or disruptive, with abrupt shifts that break sequential coherence.
  

5: Consecutive questions are consistently well-threaded, with each question clearly motivated by the prior context.

Dimension B — Transition Quality Across Topics

Rate how smoothly the interviewer transitions between topics, subtopics or sections.
1: Shifts are abrupt, un-signposted, and disruptive to conversational flow.
  

5: Shifts are clearly signposted or motivated, preserving a smooth and intelligible flow.

Dimension C — Contingent Responsiveness of Follow-ups

Rate whether follow-up questions are grounded in the interviewee’s prior responses.
  

1: Follow-ups frequently ignore prior answers, introduce unwarranted assumptions, or feel like non-sequiturs.
  

5: Follow-ups consistently demonstrate warranted uptake, building directly on what the interviewee has said.

Output format (JSON):
  

  "local_coherence": <1-5>,
  "transition_quality": <1-5>,
  "contingent_responsiveness": <1-5>,
  "brief_rationale": "1–3 sentences justifying the scores overall"
```

原檔：`prompts/06-interview-flow-evaluator.en.txt`。來源定位：`A1.SS8.SSS1.p1`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2602.21136v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
