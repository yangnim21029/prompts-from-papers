# Python 個人化家教：出題、輔導與答案評分

公開模板可用來依教材產生程式題、提供 Python 輔導與評估答案。研究的個人化選題由強化學習系統負責；出題的長篇 user prompt 和部分教學風格擴充未完整公開。

論文為 *Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning*。

作者：Chung, Angel Tsai-Hsuan、Zhang, Botong、Kung, Ling-Chieh、Bastani, Hamsa、Bastani, Osbert。

研究機構：賓州大學、國立臺灣大學。首次提交：2026-07-10；本頁依據 arXiv:2608.16907v1。

## 研究怎麼做，結果如何

2025 年 1–6 月在臺北十所高中推行約五個月 Python 課程。1,047 人參與，依預註冊條件排除退課、作弊標記或不可比樣本後分析 770 人；學生個別隨機分到 RL 自適應練習或固定題序。兩組教材、GPT-4o chatbot 與基礎 prompting 相同，另有隨機教學風格設計；最終為現場無 AI 書面認證考試。

自適應題序的 ITT 成績差為 +.156 SD（p<.05）；控制基線特徵、學校與年級後為 +.150 SD（p<.05）。加入隨機教學風格控制後估計仍約 +.145 SD（p=.026）。這是「同樣 AI tutor 加上更佳題序」相對固定題序的結果，不能稱為 AI 勝過真人或無 AI。

介入整合題序模型、行為紀錄、課程、出題驗證與 tutor，單抄公開 prompt 無法重現 +.15 SD。分析限合規可比樣本；中介分析對投入時間的解讀還需額外假設。出題 Figure 11 只公開 system component，長 user prompt 明確省略；Figure 12 只是共用基礎 tutor 指令，三種完整風格 variant 未附。

## 公開材料與使用方式

下方保留作者公開的模板原文，輸入資料、變數與輸出格式依各段說明。

## 原始 prompt 與配套材料

### 1. Python 出題：RAG system prompt

提供主要與補充教材；需要另備輸出格式的 user prompt、測試程式與人工審核。

需要提供：主要教材 MAIN_DOCUMENT_TEXT；補充教材 ADDITIONAL_DOCUMENT_TEXT。

用途：出題。原文範圍：完整保留 Figure 11 公開的 system component；Appendix A.2 明確省略較長的 user prompt，因此這不是完整出題請求。

```text
You are a knowledgeable AI assistant designed to help generate questions based on educational content.
Main content:
{MAIN_DOCUMENT_TEXT}

Additional content:
{ADDITIONAL_DOCUMENT_TEXT}

Your goal is to create well-structured, meaningful, and educational coding questions based on the content provided.
You may combine the concepts taught in the additional contents with the main content for generating unique and insightful questions.
You should always ensure the correctness of your output and follow the question generation format carefully.
When answering, adhere strictly to Python programming conventions and ensure the output format is clean and structured.
```

Figure 11: System prompt for RAG practice problem generation pipeline.

原檔：`rag-problem-generator-system-excerpt.md`。來源定位：`A1.F11`。

### 2. Python 家教：共用基礎 system prompt

此為所有條件共用的基礎指令；實驗另有教學風格擴充與問題／答案脈絡。

需要提供：學生提問；目前練習題與難度；參考解答程式或答案。

用途：教學。原文範圍：完整保留 Figure 12 的共用基礎指令；各教學風格的完整擴充版本及組裝後的 user message 未隨論文公開。

Base system prompt.

You are a Python tutor. Your goal is to help students develop a deeper understanding of Python while keeping them focused on learning. Keep responses brief, concise, and to the point---exercise restraint.

Explain to me like I’m a middle school student and make sure to use the solution code provided in the context.

Figure 12: Common base system instruction (used in all conditions)

原檔：`python-tutor-base-system-excerpt.md`。來源定位：`A1.F12`。

### 3. 程式提交評估：計算有意義的修改次數

逐次比較提交內容，僅計入邏輯、方法或功能的有意義修改，輸出整數。

需要提供：歷次程式提交 coding_history；題目內容 question.content；提交次數上限 len(coding_history_list)。

用途：評分。原文範圍：完整公開的 Figure 14 任務提示。

Prompt for counting meaningful attempts

```text
You are given a list of coding history for a user which contains various code submissions the question below.

{coding_history}

Question:

{question.content}

Count the number of meaningful code submissions in the user’s history.

For each code submission in the history, compare it with its previous submission and count it as 1 ONLY if it introduces a meaningful change in terms of logic, approach, or functionality.

The same code as the previous submission or like small typos, formatting, or minor variable name changes without changing logic, or provide empty or nonsense code should be counted as 0.

The final count must be an integer between 0 and {len(coding_history_list)}. Return only the integer value with no additional text.
```

Figure 14: Prompt used to ask an LLM to count the number of meaningful submissions.

原檔：`meaningful-code-attempt-counter-excerpt.md`。來源定位：`A2.F14`。

### 4. Python 家教：出題與教學提示的組裝脈絡

保存原文對缺少 user prompt、兩題一批、JSON／中英雙語輸出、測試驗證，以及三種 pedagogy 風格的說明。

需要提供：主要與補充教材；既有題目清單；學生提問；目前題目與相關資料；參考解答程式。

用途：required context。原文範圍：保存原文程序說明，不是額外的完整 prompt。因保留完整來源章節，部分 Figure 11／12 文字會重複出現。

#### A.2 RAG System for Problem Generation

We generate Python programming questions based on instructional materials using the RAG-based LLM pipeline shown in Fig. 10. For each generation request, we prompt the LLM with (i) the main instructional content, (ii) optional additional content (e.g., prior modules), and (iii) a list of existing questions to discourage duplicates. The model is instructed to output a JSON object containing two coding questions (in English with a traditional Chinese translation), along with a template solution stub, a working sample solution, and a comprehensive assert-based test suite. To encourage variety in the generated questions (e.g., different scenarios and wording), we use sampling settings that allow some randomness (temperature = 1.0, top-p= 0.7, top-k= 200).

The system prompt provides the educational content and high-level role instructions, while the user prompt specifies the required output format and constraints (difficulty levels, bilingual problem statements, and test-suite requirements); we show the system prompt in Figure 11 (we omit the user prompt due to its long length). We generate questions in batches of two.

Figure 10: Human-AI RAG pipeline for practice problem generation. Course materials and past exams are retrieved as reference contents for an LLM (ChatGPT) to generate programming questions, solutions, and test cases. Each generated output is validated using a Python script that checks functional correctness and consistency. When validation fails, a secondary LLM (Claude) iteratively revises the components until they pass. Teaching assistants then review finalized questions for clarity and quality before deployment.

```text
You are a knowledgeable AI assistant designed to help generate questions based on educational content.
Main content:
{MAIN_DOCUMENT_TEXT}

Additional content:
{ADDITIONAL_DOCUMENT_TEXT}

Your goal is to create well-structured, meaningful, and educational coding questions based on the content provided.
You may combine the concepts taught in the additional contents with the main content for generating unique and insightful questions.
You should always ensure the correctness of your output and follow the question generation format carefully.
When answering, adhere strictly to Python programming conventions and ensure the output format is clean and structured.
```

Figure 11: System prompt for RAG practice problem generation pipeline.


#### A.3 GenAI Chatbot Tutor

#### Tutor integration and shared context.

Students interacted with our GenAI tutor (powered by OpenAI’s GPT-4o model) embedded in the learning platform during practice. The tutor was available in both the treatment (RL sequencing) and control (fixed sequencing) conditions, and the tutoring model and prompting pipeline were held constant across conditions.

At each practice step, the tutor received a user prompt formed by concatenating the student’s query with the current practice problem, relevant metadata (e.g., difficulty), and the sample solution code and/or answer key. The tutor was instructed in the system prompt (see Fig. 12) to keep responses brief and to explain concepts at a middle-school level. This design enabled the tutor to provide accurate, targeted hints while enforcing a strict “no direct answers” policy.

Base system prompt.

You are a Python tutor. Your goal is to help students develop a deeper understanding of Python while keeping them focused on learning. Keep responses brief, concise, and to the point---exercise restraint.

Explain to me like I’m a middle school student and make sure to use the solution code provided in the context.

Figure 12: Common base system instruction (used in all conditions)

#### Pedagogy randomization.

The focus of this paper is on RL-based sequencing of practice problem difficulty. However, we also randomized the AI tutor’s system prompt in this study (see our pre-registered plan in D.4).
All our pedagogy prompts shared the following instructions: (i) do not provide direct answers or full code; (ii) diagnose whether the student’s difficulty is problem formulation versus Python syntax/logic and respond accordingly; (iii) keep responses concise; (iv) maintain role consistency; and (v) respond in Traditional Chinese when the student writes in Chinese. They only differed in pedagogical emphasis. We find no meaningful or statistically significant differences across these pedagogy conditions in exam performance or engagement outcomes; accordingly, we do not focus on pedagogy comparisons in this paper. We show that our results are robust to this additional randomization in F.1.

原檔：`prompt-assembly-context-excerpt.md`。來源定位：`A1.SS2; A1.SS3`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2608.16907v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
