# 目標設定：把模糊願望寫成具體行動

FeedbackBot 根據使用者寫下的目標追問，並透過 got_specific_goal 函式接收具體目標。公開範例另有固定引導語與挑戰程度建議。它們分屬不同聊天機器人條件，完整狀態流程需另行搭建。

論文為 *Supporting Effective Goal Setting with LLM-Based Chatbots*。

作者：Michel Schimpf、Sebastian Maier、Anton Wyrowski、Lara Christoforakos、Stefan Feuerriegel、Thomas Bohné。

研究機構：University of Cambridge、LMU Munich、Munich Center for Machine Learning (MCML)、Technical University of Munich。首次提交：2026-02-09；本頁依據 arXiv:2602.08636v1。

## 研究怎麼做，結果如何

預註冊五組隨機實驗。英國 Prolific 招募 576 人，33 人未通過注意力檢查，分析 543 人；五組為固定訊息 ControlBot、規則式 GuidanceBot、加入建議的 SuggestionBot、加入回饋的 FeedbackBot，以及全部功能 GenBot。對話以 goal、goal type、specific goal、challenging goal、action、cue 等狀態推進。兩位編碼者評目標明確度與 implementation intention 品質，另收主觀難度、承諾等指標。

相較 GuidanceBot，FeedbackBot 提高目標明確度（r=.29，p<.001）與 if–then 計畫品質（r=.50，p<.001）；難度差異不顯著。

GuidanceBot 相較固定指示 ControlBot，明確度 r=.23、p=.001；計畫品質 r=.40、p<.001。

自動產生建議沒有帶來超越引導本身的顯著改善；回饋與引導是較有支持的設計特徵。

測的是當次目標文字品質，沒有追蹤真實目標完成率。

主觀承諾或行動意圖並非隨 chatbot 複雜度同步提高；不能把較完整的目標等同更高動機。

公開文章只展示部分狀態提示與固定指示；完整 backend 雖公開但未查到授權，未在此重發布。

## 公開材料與使用方式

本頁五份 prompt／格式範例取自 CC BY 4.0 論文。完整 backend 程式庫未提供 LICENSE，因此不在此重刊。SuggestionBot 原文中的拼字與字串符號照原樣保留。

FeedbackBot prompt 必須配合 got_specific_goal function schema；ControlBot 兩則為依序傳給人的固定指示；SuggestionBot 是單一挑戰程度階段，須填好 Python 日期與目標變數。

## 原始 prompt 與配套材料

### 1. System Prompt — Specificity (FeedbackBot)

需要提供：{goal} 與對話歷史。

用途：系統指令。原文範圍：完整公開範例；文章沒有把全部狀態流程印出來，不代表完整五種 chatbot。

```text
The user just decided to pursue the goal: '{goal}'.
Help the user make the goal more specific.
A specific goal must include:
1) a clear and specific time (e.g., an exact date like 1st December),
2) a concrete, measurable outcome (e.g., run 5k in under 20 minutes).

If any element is missing, ask one targeted question at a time like:
- "I think your goal is missing a concrete time. When exactly do you want to achieve it?"
- "I think your goal is missing a measurable outcome. How could you measure it?"

You do not give any examples or suggestions in your answer.
When summarizing the user's goal, keep it short and do not add new information.
As soon as you identify a specific goal, call the function 'got_specific_goal' with the finalized goal string as the parameter.
```

原檔：`prompts/feedback-specific-goal.txt`。來源定位：`Figure 4 (left)`。

### 2. Function Schema

需要提供：前一步選定的個人目標。

用途：輸出格式。原文範圍：完整公開範例；文章沒有把全部狀態流程印出來，不代表完整五種 chatbot。

```json
{
  "type": "function",
  "function": {
    "name": "got_specific_goal",
    "description": "Call if user gives a specific goal.",
    "parameters": {
      "type": "object",
      "properties": {
        "specific": {
          "type": "string",
          "description": "Finalized goal, without adding information"
        }
      },
      "required": ["specific"]
    }
  }
}
```

原檔：`prompts/specific-goal-function.json`。來源定位：`Figure 4 (right)`。

### 3. First Message Control-Bot

需要提供：前一步選定的個人目標。

用途：participant-instruction。原文範圍：完整公開範例；文章沒有把全部狀態流程印出來，不代表完整五種 chatbot。

```text
In the following, you’ll receive advice on how to formulate your goal and the corresponding action to increase the likelihood of achieving it.  Read carefully, then type your answers below.

To help you define a goal that increases your chances of success, please identify a current goal you want to achieve.

When you have chosen your goal, please specify whether it is a learning or performance goal.
For  a new, complex task you should choose a learning goal in order to identify a good strategy to achieve your goal first. Otherwise choose a performance goal to increase your performance on that tasks.

Learning Goal Definition: A learning goal focuses on developing a set number of strategies, processes, or procedures in order to master a task.
Example: Identify three swimming techniques to improve speed by Monday.

Performance Goal Definition: A performance goal centers on achieving a specific outcome.
Example: Swim 100 meters in under 2 minutes by December 1st.

For the best results, your goal should be both specific and challenging. Specific, challenging (yet achievable) goals significantly boost performance and goal attainment.

Specific Goals Require:
- Clear Time Frame: A precise deadline or time frame.
- Concrete Measurement: A clear and measurable outcome.

Challenging Goals Are: Difficult enough to push your limits but still realistic and attainable.

**Based on the guidance, please define your goal here:**
```

原檔：`prompts/control-first-message.txt`。來源定位：`Appendix E, Figure 6 (left)`。

### 4. Second Message Control-Bot

需要提供：前一步選定的個人目標。

用途：participant-instruction。原文範圍：完整公開範例；文章沒有把全部狀態流程印出來，不代表完整五種 chatbot。

```text
Next, create an action plan based on your goal using the principle of implementation intentions. 

Implementation intentions are structured as if-then plans that specify a situation (the "if" condition) and the behavior to be performed (the "then" action).

Example: If I come home from work on Monday, then I’ll pack my swim gear and go swimming.

**Based on the guidance, please define your implementation intention here:**
```

原檔：`prompts/control-implementation-intention.txt`。來源定位：`Appendix E, Figure 6 (right)`。

### 5. Prompt to Generate suggestions for more challenging goals

需要提供：{summary.specific}、當前日期／星期／時間。

用途：系統指令。原文範圍：完整公開範例；文章沒有把全部狀態流程印出來，不代表完整五種 chatbot。

```text
The user just set the goal of: '{summary.specific}'\n"

Generate 3 different examples of how the user could makes the goal below more challenging while still achievable. This most challenging should be today.

You do that by either increasing the difficulty of the goal or by shortening the time frame. But not by adding something.

Say something in the format of:
'You for example could make your goal challenging by:
1. Already choosing a strategy today. (only if the user didn't already plan to do it today)
2. doing ... (other shorter timeframe)
3. or increasing the difficulty by identifying x strategies before choosing one.'

But use examples that make sense fore the goal the user set.

Keep it short maximum 10 words.

If you need todays date is:{datetime.now().strftime('%Y-%m-%d')}, the weekday is {datetime.now().strftime('%A')}, and the time is {datetime.now().strftime('%H:%M')}
```

原檔：`prompts/suggestion-challenging-goal.txt`。來源定位：`Appendix E, Figure 7`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2602.08636v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
