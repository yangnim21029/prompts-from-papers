# 市場研究：擷取需求與建立消費者分身

公開模板可從訪談擷取需求、編碼廣度和深度，再將人物資料與訪談加入數位分身。另有廣告宣稱、郵件和影片回應任務及評估模板。完整商業訪談平台的主持指令沒有公開。

論文為 *AI-Moderated Interviews for Market Research and Digital Twins Calibration*。

作者：Yuting Deng、Jingxuan Liu、Olivier Toubia、Naman Jain。

研究機構：Columbia University（哥倫比亞大學）、University of Pennsylvania（賓州大學）。首次提交：2026-09-24；本頁依據 arXiv:2609.29143v1。

## 研究怎麼做，結果如何

研究共有 317 人：AI 訪談 139 人、靜態訪談 154 人、真人訪談 24 人。AI 與靜態條件隨機分配，真人條件另行招募。需求分析另做每組 24 份訪談的配對重抽樣比較；數位分身則用未放入建立資料的行銷任務驗證。

配對到每組 24 份訪談時，每份訪談平均擷取的需求數為 AI 7.48、靜態 5.01、真人 7.08。AI 相較靜態取得更多需求，但 AI 與真人沒有可靠的高低順序。較豐富的 AI 訪談資料未帶來比靜態訪談更準確的量化分身預測。

真人組樣本小且非同批隨機分配；AI更豐富的訪談未帶來比靜態訪談更準確的量化分身預測；真人訪談情感投入較高；一位作者為合作AI公司CEO。

## 公開材料與使用方式

公開範圍涵蓋需求擷取、數位分身與評估，沒有完整商業主持系統指令。行銷刺激中的圖片、影片、品牌與受訪者資料需另備。

## 原始 prompt 與配套材料

### 1. 訪談廣度與深度編碼

按主題判斷是否出現及深度，保留證據；主題碼本須另外提供。

需要提供：逐字稿、指定主題碼本與目前問題。

用途：資料分析。原文範圍：全文。

```text
[Block-specific introduction, e.g., “You are coding a respondent’s relationship with windows & doors and how they feel about replacement, for breadth and depth.”]
The coding unit is one respondent \times this open-ended block.
For AI-moderated data, use the full adaptive exchange for this block.
For audio-only data, use the pooled fixed prompts for this block.

This block’s predefined interview objective is: [the block’s moderator objective from Appendix A].
Use the [N]-theme codebook below, which decomposes that objective. For each theme: decide whether it is present (0/1); assign a depth score from 0 to 4; provide a short supporting quote (verbatim from the respondent only, not the interviewer); provide a brief reasoning explaining WHY you assigned that depth score.

## Depth rubric.
0 = absent — The theme is not meaningfully present.
1 = mention only — Present but only as a brief mention or label. No real detail, explanation, process, or outcome.
2 = minimal elaboration — Present with one layer of development: one concrete detail, one reason, one example, or one simple action/outcome.
3 = clear elaboration — Clearly developed with at least two kinds of substantive support (specific details, explains why, describes action, gives comparison, describes consequence).
4 = rich elaboration — Developed in a rich, multi-part way with several specifics and strong sense of reasoning, process, or consequences.

## [N] Themes.
[The block’s themes, one per line, each with its one-line inclusion/exclusion definition; Table C lists them.]

## Coding Rules.
1. A theme can only have depth >0 if it is present.
2. If absent: present=0, depth=0.
3. If present: assign depth 1, 2, 3, or 4.
4. Use broad coding: a theme covering several related specifics still counts as ONE theme.
5. Do not count interviewer wording by itself. Only code what the respondent actually expresses.

## Output Format.
Return ONLY valid JSON with this exact structure (no markdown, no commentary):
{“themes”: {“<theme>”: {“present”: 0_or_1, “depth”: 0-4, “evidence”: “short quote”, “reasoning”: “why this depth score”}, …}, “breadth_count”: <sum of present>, “mean_depth_present_themes”: <mean depth across present themes only>, “total_depth”: <sum of all depths>}
```

原檔：`prompts/01-breadth-depth-coder.en.txt`。來源定位：`A3.SSx1.p2.1`。

### 2. 整合五位編碼器的判斷

檢查五份編碼，依原文規則形成最終判斷。

需要提供：同一回覆、碼本、五份獨立編碼。

用途：評分。原文範圍：全文。

```text
You are the lead qualitative analyst adjudicating a panel of 5 independent coders who each coded the SAME response against a [N]-theme codebook (each theme: present 0/1 and depth 0–4). Produce the consensus coding by MAJORITY RULE: a theme is PRESENT iff at least 3 of the 5 coders marked it present (present=1). If present, its DEPTH is the median of the depth scores from the coders who marked it present (round half up to an integer 1–4). If absent, depth=0. Then compute breadth_count = number of present themes, mean_depth_present_themes = mean depth across present themes only (0 if none), total_depth = sum of all depths. Return ONLY JSON with this exact structure: {“themes”: {“<theme>”: {“present”: 0_or_1, “depth”: 0-4}, …}, “breadth_count”: <int>, “mean_depth_present_themes”: <float>, “total_depth”: <int>}
```

原檔：`prompts/02-coding-adjudicator.en.txt`。來源定位：`A3.SSx1.p4.1`。

### 3. 從訪談擷取顧客需求

以 Voice-of-the-Customer 方式擷取需求，分清需求、具體功能與偏好，依指定 JSON 回傳。

需要提供：同一受訪者在四個開放問題區塊的回答。

用途：資料分析。原文範圍：全文。

```text
You are a Voice-of-the-Customer analyst extracting Customer Needs (CNs) from a respondent’s interview about window/door replacement.

A Customer Need is an abstract “job to be done” that states an underlying benefit the customer wants, articulated at a level that guides product/marketing decisions, NOT a specific product feature, a solution, an opinion, or a restatement of the question. It must be grounded in what this respondent actually expressed (no hallucination, no generic needs they did not raise).

Examples of well-formed CNs: “Confident the new windows will lower my energy bills”; “Able to trust the installer will not damage my home”; “Assured the product will last decades without maintenance”.

From the respondent text below, extract the distinct Customer Needs this respondent expressed. Return ONLY JSON: {“customer_needs”: [“need 1”, “need 2”, …]}. Return [] if none are clearly expressed. Do not invent needs that are not grounded in the text.
```

原檔：`prompts/03-customer-needs.en.txt`。來源定位：`A4.p2.1`。

### 4. 配對評估訪談資訊品質

比較兩份採購旅程回覆所含的消費者洞見。

需要提供：相同消費者類型的兩份回答。

用途：評分。原文範圍：全文。

```text
You are comparing two consumer journey responses from homeowners about replacing windows or doors. Both respondents have the same profile (same consumer status). Your job is to compare the quality of their answers on four dimensions.

Important rules: Compare only the CONTENT of the answers, not grammar. Do NOT automatically reward verbosity. A longer answer is not necessarily better. One answer may combine multiple follow-up responses from the same person — do not favor it simply for being longer. Only reward it if the additional content truly adds breadth, depth, richness, or informativeness. If the two responses are very similar on a dimension, return “Tie”.

Dimensions:
1. BREADTH: Which response covers a wider range of relevant aspects or topics?
2. DEPTH: Which response goes into more detail or explanation?
3. RICHNESS: Which response feels fuller, more textured, and more developed?
4. INFORMATIVENESS: Which response provides more useful and concrete information?

For each dimension, return exactly one of: “A”, “B”, or “Tie”. Also provide a very short reason (one sentence). Return JSON only:
{“breadth_winner”: …, “breadth_reason”: …, “depth_winner”: …, “depth_reason”: …, “richness_winner”: …, “richness_reason”: …, “informativeness_winner”: …, “informativeness_reason”: …}
```

原檔：`prompts/04-interview-quality-judge.en.txt`。來源定位：`A8.p2.1`。

### 5. 建立數位分身角色

作為 system prompt，再接上該受訪者的資料與後續任務。

需要提供：人口統計、原始訪談、偏好與經驗資料。

用途：模擬。原文範圍：全文。

```text
You are the Digital Twin of a specific human. Your job is to think, react, and answer survey/interview questions as that human would based on their raw data, which includes their answers to both closed ended questions and open ended questions. This raw data reflects what the person has said, selected, expressed, or revealed. Use it as behavioral evidence, not as a script to copy.

# Behavioral realism rules

1. Humans are not perfectly logical. Feel free to express small contradictions, emotional responses, uncertainty, convenient shortcuts, context-driven shifts, implicit biases.

2. Use heuristics, not perfectly reasoned logic. Reflect familiarity bias, impulsivity or overthinking, laziness or conscientiousness, mood-driven variation, risk aversion or risk taking.

3. Avoid LLM-like behaviors. Do not become overly rational, balanced, optimistic, consistent or polished. Think and speak like the simulated person — messier, subjective, emotional, imperfect, contextual.

4. Treat the raw data as evidence, not a script. Infer the likely human response pattern behind the data.

5. Embrace micro-variability. Humans do not answer the same way every time.

6. Use both data sources together. Closed-ended Q&A provides explicit anchors; verbatim log provides nuance.

7. When the sources differ, resolve like a human — preserve realistic messiness.

# Reasoning mode (internal)

Before producing output, silently consider how this person would think and feel. Do not output reasoning. Only produce the final JSON.

# Output rules

Return valid JSON only.
```

原檔：`prompts/05-digital-twin-system.en.txt`。來源定位：`A10.SSx1.p2.1`。

### 6. 預測產品利益訴求排序

預測同一位受訪者對指定訴求的排序與理由。

需要提供：數位分身脈絡與三項行銷訴求。

用途：模擬。原文範圍：全文。

```text
Now predict how this respondent would answer the following survey task.

[Q1] Question A1 (ranking): Below are three benefit claims about [Brand] windows. [Brand] is a major window replacement company in the United States. Please rank the benefits based on how attractive you find each message. (1 = Resonates the most, 3 = Resonates the least)

Options:

1. [Brand] windows won’t warp, bow, crack, bend or wobble for 30 years, leading vinyl windows fail in less than 20 years

2. [Brand] windows reduce drafts in your home 80% more than leading vinyl windows

3. [Brand] windows will increase the value of your home 25% more than builder-grade vinyl windows

[Q2] Question A2 (open-ended): Please explain your ranking and why you found your top-ranked selection the most attractive over the others.

Return your answer as valid JSON:

{“A1_ranking”: [“most attractive option text”, “second option text”, “least attractive option text”], “A1_rationale”: “…”, “A2_explanation”: “first-person explanation”, “A2_rationale”: “…”}
```

原檔：`prompts/06-benefit-claims.en.txt`。來源定位：`A10.SSx2.p1.1`。

### 7. 預測材質疑慮訴求排序

依研究中的窗戶與材質情境預測排序及理由。

需要提供：數位分身脈絡與門窗材質相關訴求。

用途：模擬。原文範圍：全文。

```text
Now predict how this respondent would answer the following survey task.

[Q1] Question B1 (ranking): Below are several statements about vinyl windows, a popular type of household window. Please imagine that the windows you currently have are vinyl windows and rank the following statements based on how concerning they are to you. (1 = The most concerning, 3 = The least concerning)

Options:

1. Vinyl windows are 10x more likely to have operation and performance issues within the first 10 years

2. Vinyl windows exterior colors begin to fade and white begins to yellow in less than 5 years

3. Due to vinyl warp, your vinyl windows won’t latch over time (security risk)

[Q2] Question B2 (open-ended): Please explain your ranking and why you found your top-ranked selection the most concerning over the others.

Return your answer as valid JSON:

{“B1_ranking”: [“most concerning option text”, “second option text”, “least concerning option text”], “B1_rationale”: “…”, “B2_explanation”: “first-person explanation”, “B2_rationale”: “…”}
```

原檔：`prompts/07-vinyl-claims.en.txt`。來源定位：`A10.SSx3.p1.1`。

### 8. 預測對直郵廣告的回應

原研究會把圖片直接附在請求中；純文字模板未包含圖片。

需要提供：數位分身脈絡與廣告圖片。

用途：模擬。原文範圍：全文。

```text
Now predict how this respondent would answer the following survey task.

[Q1] The image above shows a direct mail campaign. Please view it, then indicate how much this respondent would agree or disagree with each statement about this campaign. (Scale: 1 = Strongly Disagree, 5 = Strongly Agree)

1. This mailer grabs my attention.

2. The main message of this mailer is clear.

3. This mailer makes me want to learn more about the brand.

4. This mailer feels relevant to me and my needs.

5. I like this mailer overall.

[Q2] Then answer this open-ended question exactly as this person would, using first person and this person’s tone and perspective: “What stood out to you most about this mail piece, and what (if anything) could be improved?”

Return your answer as valid JSON:

{“ratings”: [score1, score2, score3, score4, score5], “feedback”: “first-person response to the open-ended question, using this person’s tone and perspective”}

where each score is an integer from 1 to 5.
```

原檔：`prompts/08-mailer.en.txt`。來源定位：`A10.SSx4.p1.2`。

### 9. 預測對廣告影片的回應

原研究會把影片直接附在請求中；需一併提供刺激材料。

需要提供：數位分身脈絡與廣告影片。

用途：模擬。原文範圍：全文。

```text
Now predict how this respondent would answer the following survey task.

[Q1] The video above shows a TV commercial. Please watch it, then indicate how much this respondent would agree or disagree with each statement about this commercial. (Scale: 1 = Strongly Disagree, 5 = Strongly Agree)

1. This commercial grabs my attention.

2. The main message of this commercial is clear.

3. This commercial makes me want to learn more about the brand.

4. This commercial feels relevant to me and my needs.

5. I like this commercial overall.

[Q2] Then answer this open-ended question exactly as this person would, using first person and this person’s tone and perspective: “What stood out to you most about this commercial, and what (if anything) could be improved?”

Return your answer as valid JSON:

{“ratings”: [score1, score2, score3, score4, score5], “feedback”: “first-person response to the open-ended question, using this person’s tone and perspective”}

where each score is an integer from 1 to 5.
```

原檔：`prompts/09-commercial.en.txt`。來源定位：`A10.SSx5.p1.2`。

### 10. 加入相似廣告的既有評分

作為校準條件的插入段落，須填入該受訪者的已知答案。

需要提供：另一則廣告或影片的題目、評分。

用途：輸入脈絡。原文範圍：全文。

```text
# This person was previously shown {the other mailer/commercial} and gave these ratings:

(Scale: 1 = Strongly Disagree, 5 = Strongly Agree)

1. {statement} {score}  … 5. {statement} {score}

When asked “{the open-ended question}”, the person said:

“{feedback}”

Use these ratings and feedback to understand this person’s response tendencies and perspective.
```

原檔：`prompts/10-calibration-ratings.en.txt`。來源定位：`A10.SSx6.p2.2`。

### 11. 加入既有評分與理由

在分身原有資料中加入相似任務的答案和理由。

需要提供：另一則刺激的評分與開放式理由。

用途：輸入脈絡。原文範圍：全文。

```text
# This person previously evaluated {the other mailer/commercial}:

(Scale: 1 = Strongly Disagree, 5 = Strongly Agree)

1. {statement} {score}  … 5. {statement} {score}

When asked “{the open-ended question}”, the person said:

“{feedback}”

# This person was then shown {the target mailer/commercial} and when asked “{the open-ended question}”, said:

“{target feedback}”

Based on all of the above, predict this person’s ratings for {the target mailer/commercial}.
```

原檔：`prompts/11-calibration-ratings-reasons.en.txt`。來源定位：`A10.SSx6.p3.2`。

### 12. 加入既有訴求排序

提供同一受訪者在另一組題目的排序資料。

需要提供：另一組行銷訴求與真實排序。

用途：輸入脈絡。原文範圍：全文。

```text
# This person was previously asked to rank 3 marketing claims ({benefit claims (Claim Set A) or vinyl concern claims (Claim Set B)}).

# Their ranking (most to least attractive/concerning):

# 1. {claim} 2. {claim} 3. {claim}

# Now predict how this same person would answer a different but related ranking task.
```

原檔：`prompts/12-calibration-ranking.en.txt`。來源定位：`A10.SSx6.p4.2`。

### 13. 加入既有排序與理由

把排序和解釋一起加入校準資料。

需要提供：另一組訴求的排序與理由。

用途：輸入脈絡。原文範圍：全文。

```text
# This person was previously asked to rank {benefit claims (Claim Set A) or vinyl concern claims (Claim Set B)} and responded as follows:

Ranking (most to least):

1. {claim} 2. {claim} 3. {claim}

When asked to explain, the person said: “{explanation}”

Now predict how this same person would answer a different but related ranking task.
```

原檔：`prompts/13-calibration-ranking-reasons.en.txt`。來源定位：`A10.SSx6.p5.2`。

### 14. 只依已知理由預測排序

將解釋提供給模型，要求預測排序；用於拆解資料與推理差異。

需要提供：受訪者對指定訴求的解釋。

用途：模擬。原文範圍：全文。

```text
# This person was asked about {benefit claims or vinyl concern claims} and explained their reasoning as follows:

“{explanation}”

Based on this reasoning, predict their ranking.
```

原檔：`prompts/14-reasoning-only.en.txt`。來源定位：`A10.SSx6.p6.2`。

### 15. 編碼資料相關性與推理一致性

檢查原資料是否涉及該題，以及分身的推理與人類理由是否一致。

需要提供：訓練訪談、人類答案與分身理由。

用途：評分。原文範圍：全文。

```text
You are analyzing reasoning gaps in a digital twin study. A human did an open-ended interview (TRAINING) about their window/door experiences and brand awareness. An AI “twin” was built from that interview. Later, both the human and the twin evaluated a marketing stimulus (VALIDATION) — either ranking claims, or rating a mailer/commercial on 5 items. Analyze TWO things:

A. DATA GAP: Human validation reasoning \rightarrow training interview. Can the HUMAN’S OWN validation explanation/feedback be traced back to what they said in the interview? Rate data_traceability_score on a 0–4 scale:
4 = All validation reasoning points directly trace to specific interview statements;
3 = Most points trace; only 1 minor new point that could be inferred;
2 = About half trace, half are genuinely new reasoning;
1 = Few points trace; most introduce new themes absent from interview;
0 = No validation reasoning traces to interview content at all.

B. MODEL GAP: Twin reasoning vs human reasoning. Does the twin reason similarly to the human? Rate reasoning_similarity_score on a 0–4 scale:
4 = Twin uses essentially identical logic chains, priorities, and emphasis as human;
3 = Twin captures main reasoning with minor wording/emphasis differences;
2 = Twin mentions similar topics but reasons differently or re-prioritizes;
1 = Some thematic overlap but mostly different reasoning; fabricated points;
0 = Twin’s reasoning is entirely different or fabricated.

Respond in this exact JSON format: {“data_traceability_score”: 0-4, “reasoning_similarity_score”: 0-4}
```

原檔：`prompts/15-reasoning-fidelity.en.txt`。來源定位：`A14.SSx1.p1.1`。

### 16. 評估回應的推理方式

依公開的 System 1／System 2 規準編碼回應風格。

需要提供：一份消費者對行銷刺激的回應。

用途：評分。原文範圍：全文。

```text
You are scoring reasoning style in a consumer research study about windows and doors. You will see ONE response about a marketing stimulus. Score it on the System 1 vs System 2 scale:

0 = Pure System 1 (intuitive/reactive). Gut reaction, no elaboration. “I just didn’t like it.” “It looked nice.”
1 = Mostly System 1. Intuitive reaction with minimal explanation. “I don’t like the sound of it, feels cheap.” “The handwriting caught my eye.” Driven by immediate sensory or emotional impression.
2 = Mixed. Both intuitive reactions and some analytical reasoning. “It felt professional, and the financing makes sense for what you get.”
3 = Mostly System 2 (deliberative/analytical). Structured reasoning with mild personal preference. “I’m concerned about performance because we live in Florida — energy efficiency matters most.”
4 = Pure System 2. Fully deliberative and systematic. No intuitive or emotional language. “Comparing warranty, energy rating, cost, and contractor experience, the draft claim ranks highest.”

Respond in this exact JSON format: {“system”: 0-4}
```

原檔：`prompts/16-response-style.en.txt`。來源定位：`A14.SSx2.p1.1`。

### 17. 分類人類與分身的理由焦點

把回應中的理由逐點分類，用於比較兩者注意的面向。

需要提供：人類與分身的兩份回應。

用途：資料分析。原文範圍：全文。

```text
You are analyzing reasoning in a consumer research study about windows and doors. You will see TWO responses about a marketing stimulus. For EACH response, identify every distinct reasoning point and classify it into exactly one category:

Categories:
sensory: Reacting to what they saw, heard, or felt in the stimulus. “I didn’t like the sound.” “The colors caught my eye.” “The handwriting looked messy.”
personal_memory: Referencing their own life, past events, household. “When we replaced our windows…” “My house is worth $1M.” “I have kids so safety matters.”
emotional: Trust, comfort, safety feelings, annoyance, excitement, values. “I feel safe.” “It bothered me.” “I don’t want to worry.” “It’s cheesy.”
feature: Evaluating specific product attributes or offer details. “Energy efficiency.” “30-year warranty.” “The discount offer.” “Draft reduction claim.”
logical: Reasoning from evidence, cause-effect, comparisons. “If it warps, then security risk.” “Vinyl fails faster so durability matters more.”
social_proof: Referencing others, reviews, professionalism, credibility. “Customer reviews.” “Looks professional.” “Trusted brand.”

Respond in this exact JSON format: {“human_points”: [{“text”: “brief quote”, “category”: “category_name”}, …], “twin_points”: [{“text”: “brief quote”, “category”: “category_name”}, …]}
```

原檔：`prompts/17-response-focus.en.txt`。來源定位：`A14.SSx3.p2.1`。

### 18. 四類訪談區塊的主題碼本

與廣度及深度編碼模板一起使用，保留各主題的定義。

需要提供：訪談區塊與其主題分類。

用途：輸入脈絡。原文範圍：全文。

```text
\TABLE

Breadth and depth codebooks for the four open-ended blocks.

Theme

What it captures

Category usage, context and feelings (3 themes)

Prior experience

Whether and how they have replaced windows or doors before, or their familiarity with the category.

General feelings

How they generally feel about replacing (dread, indifference, stress, excitement, satisfaction).

Reasons for feelings

Why they feel that way (cost, hassle, disruption, importance, a past good/bad experience).

Purchase journey (9 themes: union of the two journey variants; recently-replaced covers 8, considering covers 7)

Trigger

What initiated the need or the consideration.

Research & information search

How information was gathered (search, reviews, vendors).

People involved

Spouse, family, contractor, vendor, or neighbor.

Options considered

Brands, stores, materials, or product types weighed.

Narrowing down

How options were compared and reduced.

Decision criteria

What mattered most (price, quality, efficiency, …).

Next step

What they plan to do next (elicited in the considering variant).

Outcome evaluation

Satisfaction with the final result (elicited in the recently-replaced variant).

Counterfactual

What they would do differently (elicited in the recently-replaced variant).

Brand awareness (4 themes)

Brands top-of-mind

Which window/door brands they name unaided.

Awareness source

How they became aware of those brands (ads, word of mouth, stores, contractors).

Partner recognition

Whether they had heard of the partnering brand before today.

Partner source

How they heard of or interacted with the partnering brand.

Brand perception and satisfaction (6 themes; the prior-customer and prospect variants share these)

Overall impression

Overall impression of or associations with the brand.

Feelings about the brand

Positive, negative, or pointedly neutral sentiment.

Brand character

What kind of brand it seems and who it is for, including self-fit.

Future consideration

Whether they would consider, choose again, or recommend it.

Openness drivers

What makes them open to it (quality, warranty, reputation, referral, service).

Barriers / concerns

What holds them back (price, uncertainty, style, no current need).

Note. For a given block, breadth is the number of these themes present and mean depth is the average 0–4 elaboration across present themes, so breadth is on a per-block scale. Each block’s moderator objective is documented in Appendix A.
```

原檔：`prompts/18-codebooks-context.en.txt`。來源定位：`Appendix C codebooks`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2609.29143v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
