# 文字訪談：依訪綱追問、分類與改寫問題

這組 Jinja 模板配合同一份訪綱運作：先生成追問，再判斷是否達到條件，必要時改寫問題。填入訪談紀錄與問題脈絡前，需由程式展開模板；訪綱 JSON 也完整保留在下方。

論文為 *Can AI interview? Comparing AI-led to Human-led Chat Interviews*。

作者：Semra Guven、Tobias Gårdhus、Andreas Bjerre-Nielsen、Anna Rogers、Hjalmar Bang Carlsen。

研究機構：University of Copenhagen（哥本哈根大學）、IT University of Copenhagen。首次提交：2026-10-16；本頁依據 arXiv:2610.23149v1。

## 研究怎麼做，結果如何

41 位大學生隨機分配至 AI 或真人訪談，主題為學業上的求助經驗。AI 使用 OpenHermes 2.5（基於 Mistral 7B），以追問、二元分類與問題改寫模板配合訪綱運作。真人對照為受過訓練的非專家訪談員。

在中位訪談時間相近的條件下，AI 提出超過兩倍的問題，取得約 65% 更多受訪者文字。兩組回答幾乎都切題，研究未檢出具體程度的差異。資料量增加不等於洞見品質提高，未檢出差異也不能當作統計等效。

正面成效主要是資料量，不代表洞見品質更高；樣本小、對照非專家訪談員；僅AI組有受訪者跳題；未檢出差異不能當成等效證明。

## 公開材料與使用方式

五份 Jinja 模板、完整訪綱及 AGPL-3.0 授權依固定 commit 保存。

## 原始 prompt 與配套材料

### 1. 追問代理的角色規則

要求一次只問一題。

需要提供：搭配追問 user prompt。

用途：訪談。原文範圍：全文。

```jinja
You are an interviewer with a lot of experience in conducting qualitative social scientific interviews. 

Your job is to ask relevant follow-up probes based on the transcript and information provided by the user. 

It is important that you only ask one question at the time.
```

原檔：`prompts/probing_agent_system_prompt.jinja`。來源定位：`prompts/probing_agent_system_prompt.jinja`。

### 2. 依訪綱與對話追問

依近期對話與建議追問提出簡短開放式問題，避免提供建議或回饋。

需要提供：question_context、interview_transcript、probes。

用途：訪談。原文範圍：全文。

````jinja
The following is the last part of a qualitative interview:

Question context:
```json
{{ question_context }}
```

Transcript:
"""
{{ interview_transcript }}
"""

Suggested probes:
```json
{{ probes }}
```

Your job is to:
- Ask a relevant follow-up question based on the transcript and the suggested probes.
- Do not ask yes/no questions, but instead ask open-ended questions that invite the interviewee to share their thoughts and experiences.
- Do not provide direct advice or feedback in your response.
- If you pick a probe from the above suggestions, you must make sure to paraphrase it so that it fits within the conversation.
- Ask only one question at a time and keep your questions brief.
````

原檔：`prompts/probing_agent_probing_prompt.jinja`。來源定位：`prompts/probing_agent_probing_prompt.jinja`。

### 3. 二元分類代理的角色規則

限制模型只回傳 0 或 1。

需要提供：搭配分類 user prompt。

用途：分類。原文範圍：全文。

```jinja
You are a classifying agents. Your job is to complete classification tasks.
The classification task is binary, so return either `0` or `1`.
```

原檔：`prompts/classification_agent_system_prompt.jinja`。來源定位：`prompts/classification_agent_system_prompt.jinja`。

### 4. 判斷回答是否符合轉題條件

依訪綱所設的分類條件與示例判斷是否進入後續問題。

需要提供：classification_examples、conversation_history、next_question_instruction、text。

用途：分類。原文範圍：全文。

````jinja
The following text is a part of a semi-structured interview. 
Your job is to classify the text as either 0 or 1 based on the following instructions.

{% if classification_examples %}
Here are some examples:
```json
{{ classification_examples }}
```
{% endif %}

Here is the previous part of the conversation:

"""interview_context:
{{ conversation_history }}
"""

The overall classification task it to identify whether the following text {{ next_question_instruction }} or not.

"""text:
{{ text }}
"""

Reply with 1 if the text {{ next_question_instruction }} and 0 if not.
````

原檔：`prompts/classification_agent_classification_prompt.jinja`。來源定位：`prompts/classification_agent_classification_prompt.jinja`。

### 5. 改寫已回答過的問題

只回傳重新表述的問題，並把前次回答納入考量。

需要提供：前次問題與已有回答。

用途：訪談。原文範圍：全文。

```jinja
That question has already been answered. Please respond with a reformulated
version of the question and nothing else, while taking the previous answer into
account.
```

原檔：`prompts/reformulation_prompts.jinja`。來源定位：`prompts/reformulation_prompts.jinja`。

### 6. 完整訪綱與分支條件

原始 JSON 保存訪綱、開場、結尾與跳題相關資料；改換研究題目時需一併調整。

需要提供：研究主題、主問題與追問條件。

用途：輸入脈絡。原文範圍：全文。

```json
{
  "provenance": {
    "note": "This file is the instrument as administered from the fourth day of data collection onward, and is the version all reported analyses use.",
    "revision": "A third substantive case, in which the student asked for help but did not receive it, was administered during the first three days and then dropped. The human interviewers rarely reached it within the scheduled half-hour slots, so retaining it would have meant comparing conditions on material only one of them regularly covered.",
    "interviews_affected": 8,
    "excluded_from_analysis": true
  },
  "framing": "In this interview, university students’ academic help seeking behavior will be investigated.\nIn the interview, we will be questioning students’ academic help seeking through two cases. First we will ask students to explain a case where they needed and received help with their studies. In the second case, students will explain a situation where they needed but did not ask for help.\n\nWith these two cases, we aim to investigate social processes and mechanisms surrounding university students’ help seeking and receiving help in the academic context. More specifically, these cases will question why students needed help, who they sought help or support from, the social situation surrounding their need, their relation to the helper(s) and students’ feelings, attitudes and behaviors.\n\nBy asking these two cases, we also want to investigate how university students navigate their social network to access resources and cope with academic challenges. We want to shed light on social context, university students’ experiences and how their social ties and relations impact their academic help seeking and getting help, as well as their attitudes and resilience in the face of academic challenges.\n\nIn the general context, the following questions will be examined: how do university students decide to ask for help, from which resources do they seek help from, what kind of help is needed the most, and students’ attitudes and attributions regarding different sources of help will be examined. It is important to note that the focus is not the outcome of help seeking but rather on students’ experiences, attitudes, and thoughts around seeking support/help. It is important to investigate the outcomes if or when they have an impact on individuals’ perceptions or behavior.",
  "introduction": "Thank you very much for taking part in our research. In this interview, we will ask you open-ended questions to investigate university students' academic help seeking behavior. It is very common for students to face various academic challenges in their studies such as understanding a concept, solving an exercise, doing a group project and so on.\n\nThere are no right or wrong answers. We are very interested in hearing your experience and perspective. The only constraint is that you must write your answers in one go, not using multiple lines.  Also, your responses will remain confidential and all personally identifiable information will be removed from publications.",
  "outro": "Thank you very much for sharing your insights and experiences. Your input is a valuable contribution to our research.",
  "evaluation_survey": {
    "id": "1656646"
  },
  "question_sections": [
    {
      "description": "In this group of questions, the aim is to understand the social situation in which university students needed help and were able to get help regarding their studies.\nMore specifically, the following will be investigated: for what reasons students need academic help, how students cognitively identify when help is needed, what social competencies they use to decide who can help best and how to approach. We will investigate what social processes and mechanisms play a role when students ask for help and receive help in an academic context.",
      "questions": [
        {
          "main_question": "Can you think of a situation where you needed academic help and got help with your studies?\n\nPlease provide a yes or no answer",
          "max_probes_n": 0
        },
        {
          "main_question": "What did you specifically need help with?",
          "max_probes_n": 0,
          "condition": {
            "type": "yes/no",
            "trigger_type": "re",
            "question_context": {
              "section": 0,
              "question": 0
            },
            "trigger_value": "no",
            "action": "skip_section"
          },
          "create_segue": false
        },
        {
          "main_question": "How did you get help?",
          "probes": [
            "Did you personally ask for help? If so, how?",
            "From whom did you get help? Can you describe the social situation?",
            "How would you describe your relation to them?",
            "How do you decide who can help best and how to approach them?"
          ],
          "max_probes_n": 5
        },
        {
          "main_question": "Who else did you consider asking for help?",
          "probes": [
            "What factors influenced your decision?"
          ],
          "max_probes_n": 2
        },
        {
          "main_question": "How did you feel after getting the help?",
          "probes": [
            "What are your expectations from the helper?"
          ],
          "max_probes_n": 2
        },
        {
          "main_question": "In general, what are the reasons you seek academic help?",
          "max_probes_n": 1
        },
        {
          "main_question": "Who do you ask to get help to resolve your academic challenges? How would you describe your relation to them?",
          "max_probes_n": 1
        }
      ]
    },
    {
      "description": "The goal is to understand the social situations where university students needed help but did not ask for help regarding their studies. More specifically, the aim is to understand why students refrain from asking for academic help, their relation to the helper, what factors affect their decision, and how this impacts their help seeking behavior will be investigated. We will investigate what social processes and mechanisms play a role when students refrain from asking for academic help even though they need it.",
      "questions": [
        {
          "main_question": "Can you think of a situation where you needed help with your studies but did not ask for it?\n\nPlease provide a yes or no answer",
          "max_probes_n": 0
        },
        {
          "main_question": "What did you specifically need help with?",
          "max_probes_n": 0,
          "condition": {
            "type": "yes/no",
            "trigger_type": "re",
            "question_context": {
              "section": 1,
              "question": 0
            },
            "trigger_value": "no",
            "action": "skip_section"
          }
        },
        {
          "main_question": "Although you did not ask for help, did you consider asking anyone for help? And if so, who?",
          "probes": [
            "How would you describe your relation to them?",
            "What were your considerations around asking for help?"
          ],
          "max_probes_n": 3
        },
        {
          "main_question": "Why did you not prefer asking for help?",
          "probes": [
            "When do you feel the most comfortable to ask for academic help?",
            "When do you feel the least comfortable to ask for academic help?"
          ],
          "max_probes_n": 4
        },
        {
          "main_question": "How did you resolve the issue?",
          "probes": [
            "Did you end up getting any help? Can you describe the social situation?",
            "How do you decide who can help best and how to approach them?",
            "When do you feel the most comfortable to ask for academic help?",
            "When do you feel the least comfortable to ask for academic help?",
            "Why did you not prefer asking for help?"
          ],
          "max_probes_n": 5
        },
        {
          "main_question": "How did you feel about this situation?",
          "probes": [
            "Under what conditions would you seek help? Can you explain why?",
            "What changes would you suggest at the university to better meet your academic needs?"
          ],
          "max_probes_n": 4
        },
        {
          "main_question": "In general, in which cases or from whom do you refrain from asking academic help? Why so?",
          "max_probes_n": 1
        }
      ]
    },
    {
      "description": "These last questions are to allow the interviewee to express any additional points.",
      "questions": [
        {
          "main_question": "Before we conclude our interview, is there anything you’d like to add or any perspectives you think we might have missed?",
          "max_probes_n": 1,
          "condition": {
            "type": "yes/no",
            "trigger_type": "re",
            "question_context": {
              "section": 2,
              "question": 0
            },
            "trigger_value": "no",
            "action": "skip_section"
          }
        }
      ]
    }
  ]
}
```

原檔：`prompts/interview-guide.json`。來源定位：`data/interview_guide.json`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2610.23149v1) · [官方程式固定版本](https://github.com/ainterviewer/can-ai-interview/tree/50f09e5eb92e47ad0d9d512ecc192f1a4a162781) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
