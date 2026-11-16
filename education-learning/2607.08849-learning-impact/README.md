# AI 學習實驗：作文評分與使用方式分類

這篇實驗讓學生自由使用 ChatGPT。下方公開材料主要供研究者評作文、分類 AI 使用方式，以及安排寫作測驗。若要使用作文評分器，還需另外準備兩篇校準文章及分數、理由。

論文為 *Experimental Evidence on the Learning Impact of Generative AI*。

作者：Contractor, Zara、Reyes, Germán。

研究機構：Middlebury College；IZA（作者研究聯盟 affiliation）。首次提交：2026-07-09；本頁依據 arXiv:2607.08849v2。

## 研究怎麼做，結果如何

2025 年春季 Middlebury 的現場監考隨機實驗；256 人報名、211 人出席第一場、205 人出席兩場。學生以 35 分鐘讀 blockchain／CRISPR／carbon capture 材料並寫約 300–500 字文章，AI 組可使用已登入的 GPT-4o 等工具，對照禁止生成式 AI。當下與平均 6.98 天後做無工具知識測驗與寫作；文章結合盲評人類與 AI 多維評分。

AI 存取的 ITT 對當下知識測驗為 +7.2 個百分點／+.28 SD（p=.021），對照平均 56.3%。一週後點估計 +3.9 個百分點／+.21 SD（p=.068），是正向但未達一般 5% 顯著門檻；不能寫成穩固顯著的持續效果。當下文章整體品質 +.34 SD（p=.024）；一週後整體品質 +.24 SD。

單一選擇性文理學院、短任務，未驗證學期成績。augmentation／automation 是學生自行選擇、研究事後分類，不能視為兩種 prompt 的隨機因果比較。研究允許自由用 AI，公開的 system prompts 主要用來評分和分類，並非造成學習差異的固定教學介入。HTML 有巨集展開錯誤，因此數字以 v2 PDF 第 3、15–19、63–69 頁核對。

## 公開材料與使用方式

作文評分部分保留公開的 system prompt 與六項評分定義；原研究兩篇校準文章及其分數、理由沒有在附錄逐字公開。兩個分類器保留完整公開指令。研究數據以 v2 PDF 核對，避開 HTML 的巨集顯示錯誤。

## 原始 prompt 與配套材料

### 1. 學習實驗：三個主題的寫作任務

保留研究的人類寫作任務；這些不是固定 AI tutoring intervention。

需要提供：指定閱讀材料；分派的科學主題與寫作題目。

用途：寫作測驗。原文範圍：保留 blockchain、CRISPR 與 carbon capture 的公開寫作題目；這些是研究參與者的作業指令，不是固定的 AI 教學 system prompt。

#### B.2 \parWriting Assessment Prompts

This appendix presents the essay prompts we developed for each of the three topics. For each topic, we designed two complementary prompts of comparable difficulty. Each prompt requires participants to analyze relationships between concepts, evaluate the relative importance of different factors, and support their analysis with specific examples. Each participant is randomly assigned to receive one prompt in Session One and the other in Session Two.24\par24\par

              

            Three participants received the same prompt in both sessions: two who completed Session Two through the emergency link and one whose Session Two login was recovered from a wrong account.

Blockchain Technology

```text
Prompt 1. “Examine how blockchain has grown beyond cryptocurrency. Analyze which two application areas have the strongest potential for transformative impact and explain the specific factors that support your analysis. Draw on examples from the reading to develop your response.”

Prompt 2. “Examine key differences between blockchain technology and traditional databases. Analyze which specific features make blockchain unique, which types of applications benefit most from these differences, and why. Support your analysis with concrete evidence or examples.”
```

Carbon Capture

```text
Prompt 1. “Analyze the three main barriers to scaling carbon capture technologies (technical limitations, economic costs, and policy challenges). Identify which barrier you believe is most critical to overcome first, how it impacts the other challenges, and what approaches might address it. Support your analysis with specific examples.”

Prompt 2. “Compare direct air capture with point-source carbon capture approaches. Analyze the specific advantages and limitations of each method, identify which contexts each approach is better suited for, and explain what factors most influence their effectiveness. Draw on evidence from the reading to support your analysis.”
```

CRISPR Gene Editing

```text
Prompt 1. “Analyze how CRISPR differs from previous gene editing technologies in terms of precision, accessibility, and versatility. Identify which two differences have been most consequential for scientific advancement, explain why these particular differences matter, and provide specific examples that demonstrate their impact.”

Prompt 2. “Examine the three main technical challenges that limit CRISPR today (delivery methods, off-target effects, and ethical considerations). Analyze which challenge is most important to address first, how it relates to the others, and what approaches show promise for overcoming it. Support your analysis with specific examples.”
```

原檔：`writing-assessment-tasks-excerpt.md`。來源定位：`A2.SS2\par`。

### 2. 文章評分：system prompt 與六項維度

每個維度單獨評分，保留 system prompt 與六項評分定義；仍須自行提供原研究未在此附錄逐字列出的校準文章。

需要提供：本次評分維度；兩篇校準文章及該維度的參照分數與理由；學生分派的主題；學生實際收到的寫作題目；待評分文章。

用途：評分。原文範圍：公開內容包含 system prompt 及評分維度定義，但不是完整 API request；兩篇必要校準文章、其分數與理由，以及組裝後的 user message 都未逐字公開。

#### B.4 \parAI Essay Grading

We complement our human grading with AI-generated scores to provide an independent assessment of essay quality. We use Anthropic’s Claude Fable 5.1 to grade each essay on the same five rubric dimensions plus the overall quality rating, using the same 0–10 scale as the Prolific graders.

For each essay, we make six separate API calls—one per grading dimension—to avoid cross-contamination between scores. Each call includes a system prompt establishing the grading context, a description of the dimension, two calibration essays with their suggested scores and rationales for that dimension, and the student essay to be graded. The calibration essays, scores, and rationales are the ones shown to human graders during training, ensuring that human and AI graders share a common scoring anchor. We ask the model for a brief justification followed by an integer score on the 0–10 scale.

The system prompt is as follows:

You are grading essays for a university research study on the determinants of learning. The essays were written by college students, who were given 35 minutes to learn about a topic and respond to a prompt. Each essay is approximately 300--500 words long. Grade each essay on a 0--10 scale. Use the two example essays, their suggested scores, and their rationales to calibrate your standards, and keep those standards consistent across essays. You may use your own knowledge to verify facts.

For each dimension, the user prompt includes the dimension name and a description of what the dimension measures. The descriptions are as follows:

Accuracy of Content. Evaluate the factual correctness and depth of understanding demonstrated in the essay. Consider whether key concepts are accurately described, whether technical details are correct, and whether the student shows genuine comprehension of the topic.

Use of Evidence &

Examples. Assess whether the essay draws on evidence from the reading the students were given. Consider how specific and well-integrated the references are.

Relevance to the Prompt. Measure whether the essay directly addresses the prompt requirements. Consider whether all parts of the prompt are addressed and whether the essay stays focused throughout.

Organization and Structure. Evaluate the essay’s organization, clarity of argument flow, and coherence. Consider whether there is a clear introduction, body, and conclusion, and whether transitions between ideas are smooth.

Writing Style and Clarity. Assess the clarity, readability, grammar, and language precision of the essay. Consider vocabulary, sentence variety, and overall polish of the writing.

Overall Essay Quality. Provide a holistic assessment of the essay’s overall quality. Consider all previous dimensions together: accuracy, evidence, relevance, structure, and writing style.

The prompt also includes the two calibration essays, the essay prompt they answer, and their suggested scores and rationales for the relevant dimension. After presenting the calibration material, the prompt provides the student’s assigned topic, the exact prompt the student was shown in that session, and the essay text. Empty essays, or those with fewer than 20 characters, are skipped and recorded as missing without querying the model.

原檔：`essay-grader-and-dimensions-excerpt.md`。來源定位：`A2.SS4\par`。

### 3. 學生提示用途分類：六類 system prompt

把學習過程中的單一提示分類為 explaining/summarizing/drafting/proofreading/editing/other。

需要提供：一則學生給 ChatGPT 的提示。

用途：分類。原文範圍：完整公開的六分類 system prompt；待分類的學生提示另行提供。

You are classifying student prompts sent to ChatGPT during a learning experiment. Students were given a reading passage on a science topic (Blockchain, CRISPR, or Carbon Capture) and asked to write an essay. Some students had access to ChatGPT during this process.

Classify each student prompt into exactly ONE of these categories:

1. Explaining concepts — Asking ChatGPT to explain, clarify, or teach a concept from the reading

2. Summarizing readings — Asking ChatGPT to summarize or condense the reading material

3. Drafting responses — Asking ChatGPT to write, draft, or generate essay text

4. Proofreading — Asking ChatGPT to check grammar, spelling, or typos

5. Editing responses — Asking ChatGPT to revise, improve, rephrase, or restructure existing text

6. Other — Anything that does not fit the above (e.g., off-topic chat, testing the tool)

Respond with ONLY the category name, exactly as written above. Nothing else.

原檔：`student-prompt-use-classifier-excerpt.md`。來源定位：`A2.SS6.SSSx1par.p4.1.1`。

### 4. 完整對話用途分類：Automation／Augmentation

把整段對話分類為 Automation、Augmentation、Mixed、Other。

需要提供：學生與 ChatGPT 的完整對話。

用途：分類。原文範圍：完整公開的四分類 system prompt；完整學生與 ChatGPT 對話另行提供。

You are classifying a full ChatGPT conversation from a learning experiment. Students were given a reading passage on a science topic (Blockchain, CRISPR, or Carbon Capture) and asked to write an essay. Some students had access to ChatGPT during this process.

Classify the overall conversation into exactly ONE of these categories:

1. Automation — The AI is doing the work FOR the student. The student asks ChatGPT to generate essay text, produce draft paragraphs, write responses, or create content that the student could paste directly into their essay. The student outsources the writing/thinking to the AI.

2. Augmentation — The AI is working WITH the student. The student uses ChatGPT to understand concepts, get explanations, ask clarifying questions, get feedback on their own writing, or check their work. The student retains ownership of the thinking and writing process.

3. Mixed — The conversation contains substantial elements of both automation and augmentation, making it hard to assign a single label.

4. Other — The conversation is off-topic, unrelated to the academic task, or consists of testing/experimenting with ChatGPT without engaging with the essay or reading material.

Respond with ONLY the category name (Automation, Augmentation, Mixed, or Other). Nothing else.

原檔：`conversation-use-classifier-excerpt.md`。來源定位：`A2.SS6.SSSx2par.p9.1.1`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2607.08849v2) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
