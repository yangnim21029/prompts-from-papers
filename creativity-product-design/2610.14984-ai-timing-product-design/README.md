# 產品發想：依團隊階段提供 AI 協助

這份產品設計助理 prompt 接收任務、目前階段與團隊最近 100 則訊息。研究用相同助理比較不同開放時機；使用模板時可參照發散、聚焦和審查三個階段。

論文為 *Too Late to Prune: Generative AI, the Screen, and Team Creative Decisions*。

作者：Difang Huang、Shumin Yu、Fadong Chen、Weihua Zhou。

研究機構：Chinese Academy of Sciences, Academy of Mathematics and Systems Science、Zhejiang University, School of Management。首次提交：2026-10-10；本頁依據 arXiv:2610.14984v1。

## 研究怎麼做，結果如何

預註冊實驗，150 個三人學生團隊招募後，兩隊因技術問題無資料，分析 148 隊／444 人。40 分鐘產品設計分發散 15 分鐘、聚焦 15 分鐘、最後審查 10 分鐘；隨機分為早期、晚期、全程、無 AI、早期加警語五組。同一 DeepSeek V3.2（temperature .1），每次提供團隊最近 100 則聊天。四位專家不知條件而評提案，主要結果先在評分者及團隊內平均。

早期組創意均分 4.88、晚期 4.52、無 AI 4.39；早期 vs. 晚期差 .356 分、g=.62、p=.018。

早期 vs. 無 AI 差 .486 分、g=.83、p=.002；全程組提升亦為 g=.83、p=.002。

晚期 vs. 無 AI 僅 g=.21、p=.43，不顯著；晚期組提交更多提案，但品質優勢未檢出。

AI 評分者能偵測有 AI 的好處，卻未偵測晚期使用的品質代價，與人類評分結果不同。

中國一所大學學生、一次短任務、單一模型，外推到真實長期專案有限。

篩選點固定在第 15 分鐘，設計沒有完全分開「篩選前後」與「經過多少時間」兩種機制。

專家評分一致性中等；四人平均 ICC 約 .44（提案）／.46（團隊），研究提供評分者子集敏感度分析。

提示本身各組相同；因果證據是存取時機安排，不是這段 system prompt 單獨勝過其他寫法。

## 公開材料與使用方式

助理 prompt 為論文公開的英文翻譯，實驗中的任務與對話為中文。另附實驗材料及創意評分規準。附錄提及的 AI evaluator system prompt 與 JSON schema 未印出全文，因此沒有另造替代版本。

## 原始 prompt 與配套材料

### 1. Product Design AI Assistant

選一組物品組合；分發散 15 分鐘、聚焦 15 分鐘、審查 10 分鐘；填當前 stage，再附團隊聊天與使用者問題。

需要提供：{task name}；{task description}；{stage}；團隊最近 100 則聊天訊息。

用途：系統指令。原文範圍：完整論文英文翻譯；原實驗使用中文，不宣稱此英文是原始運行字串。

```text
You are a Product Design AI Assistant assisting a three-person team with a product innovation design task.
Task background. Current task: {task name}. Task requirements: {task description}.
Your responsibilities. Assist the team in creative ideation, solution optimization and problem analysis. Answer
product-design questions.
Current stage and behavioral guidelines. Current stage: {stage}. If it is Stage 1, the divergence stage:
respond quickly to team requests and provide as many possible ideas as possible. If it is Stage 2, the convergence stage:
assist the team in refining product features, optimizing descriptions, evaluating market potential and screening for the
best solutions. If it is Stage 3, the final review stage: check for logical flaws, propose improvements and polish final
descriptions; conduct a final check to ensure the proposal is sound and error-free.
Response requirements. Keep responses concise and professional, within 250 characters. Use a clear structure; lists or
bullet points are recommended.
```

原檔：`prompts/product-design-assistant.txt`。來源定位：`Online Appendix B.3 Assistant Configuration`。

### 2. 實驗任務、階段與 assistant 設定

提供物品組合任務和三階段人類指令；當作 prompt 的上下文及使用流程。

需要提供：物品組合：背包與寵物配件／冰箱與日曆／鞋與地圖。

用途：必要上下文。原文範圍：完整 Experimental Materials 章節；屬上下文，不是另一套模型提示。

```latex
\section{Experimental Materials}\label{ec:materials}
%

\subsection{Tasks}
Each team received one of three object-combination tasks. The instruction read (translated from Chinese): ``Combine the
concepts of [object A] and [object B] to design one or more products or services that are both creative and
feasible.'' The pairs were (i) a backpack and a pet accessory, (ii) a refrigerator and a calendar, and (iii) shoes and a
map.

\subsection{Platform and Stages}
After logging in with their student ID, participants read condition-specific instructions, completed an interface
tutorial, and began the session after a three-second countdown that started only when all three members had finished
the tutorial. The interface had three panels: a team chat (left), the assistant panel in conditions with access
(center), and a personal draft editor that saved automatically every minute (right). The instructions (translated)
asked teams to work through three stages. \emph{Stage 1, divergence (15 minutes):} ``Brainstorm, drawing on the
features of the two objects, and generate as many preliminary product concepts as possible; you may note them briefly
in the document panel. Do not make final decisions at this stage; focus first on quantity.'' \emph{Stage 2, focusing
(15 minutes):} ``Select the best ideas from the first stage (in any number) and develop them. Settle the details of the
final proposals, name them, describe their functions (within 250 characters), and record them in the document panel.''
\emph{Stage 3, final review (10 minutes):} ``Review your proposals as a professional product designer would: check
feasibility and proofread, make sure the final proposals are fully recorded in the document panel, and choose one member
to submit.'' Each proposal was to be named and described in no more than 250 Chinese characters.

A tool notice told teams with access in which stage or stages they could use the assistant and that they could decide
for themselves how to use it; its wording was identical across conditions except for the window it named. Teams in the
no-AI condition were asked to work without online resources or external AI tools. The laboratory disabled access to
other applications and the internet; workstations were separated by partitions, and offline communication was
prohibited.

\subsection{Assistant Configuration}
The assistant was DeepSeek V3.2, called through the provider's API with the model identifier \texttt{deepseek-chat} at
temperature 0.1. Each team had its own conversation instance. Queries and responses were private to the member who
issued them; teammates saw assistant content only if it was shared in the chat. At each query, the model received the
team's 100 most recent chat messages and the following system prompt (translated):

\begin{quote}\small
You are a Product Design AI Assistant assisting a three-person team with a product innovation design task.
\emph{Task background.} Current task: \{task name\}. Task requirements: \{task description\}.
\emph{Your responsibilities.} Assist the team in creative ideation, solution optimization and problem analysis. Answer
product-design questions.
\emph{Current stage and behavioral guidelines.} Current stage: \{stage\}. If it is Stage 1, the divergence stage:
respond quickly to team requests and provide as many possible ideas as possible. If it is Stage 2, the convergence stage:
assist the team in refining product features, optimizing descriptions, evaluating market potential and screening for the
best solutions. If it is Stage 3, the final review stage: check for logical flaws, propose improvements and polish final
descriptions; conduct a final check to ensure the proposal is sound and error-free.
\emph{Response requirements.} Keep responses concise and professional, within 250 characters. Use a clear structure; lists or
bullet points are recommended.
\end{quote}

Outside a team's assigned window, the assistant panel was grayed out with an explanatory message; the no-AI condition
had no assistant panel. In the warning condition, every assistant response was followed by the statement, in bold
italics: ``AI serves only as an initial reference point and its outputs may not be accurate or comprehensive. We highly
encourage you to discuss these ideas further with your team members.''

\subsection{Incentives and Scoring Instructions}
Participants received 45 RMB for participation. Teams were told that product-design experts would score submissions
blind, primarily on creativity and feasibility and, to a lesser extent, on quantity. Members of the ten highest-scoring
teams received a bonus of up to 50 RMB each, and the strongest proposals could be forwarded to industry partners as
conceptual references. Bonus rankings used the same blinded scores as the analysis.

%
\clearpage
```

原檔：`context/experimental-materials.tex`。來源定位：`Online Appendix B.1–B.4`。

### 3. Creativity rubric and composite

依 originality quality／quantity、naming bonus、appropriateness、elaboration、text quality 評分；原文附加權公式。

需要提供：產品提案；同一任務的所有提案。

用途：評分規準。原文範圍：完整公開評分規則。I.1 只描述 LLM evaluator 的設定，未附完整 system prompt 或 JSON schema，不另行補造。

```text
D.1 Creativity: Rubric and Composite

Submissions were grouped by task and numbered within task. Four raters scored every proposal in every submission
while blind to condition and team. Each rater completed one task before moving to the next and read all proposals in a
task before scoring any of them. The rubric was:

•

Originality quality (1–7): how novel and surprising the proposal is, beyond obvious combinations of the
two objects.

•

Originality quantity: the number of distinct valid features, deduplicated within the submission, converted
to points (1 feature =2, 2 =3, 3 =5, 4 =6, ≥ 5=7).

•

Naming bonus (0, 0.5, or 1) for a creative product name.

•

Appropriateness (1–7): usefulness, feasibility, and fit with a plausible user need.

•

Elaboration (1–7): how detailed and well developed the proposal is. Because of the length limit, longer
text was not rewarded; concise descriptions that make the functions understandable suffice.

•

Text quality (1–7, supplementary): organization, readability, and coherence.

The composite is Originality =0.90× quality + 0.10× quantity score + naming bonus, and Creativity
=0.70× Originality + 0.15× Appropriateness + 0.15× Elaboration. Team scores average each rater’s
proposal scores within team and then average across raters.
```

原檔：`prompts/creativity-rating-rubric.txt`。來源定位：`Online Appendix D.1`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2610.14984v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
