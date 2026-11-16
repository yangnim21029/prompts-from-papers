# 人格適配教學：模擬學生與選擇教學策略

PATS 先判斷學生的人格特徵，再選擇教學回應。公開材料包含學生模擬器、普通與人格適配教師基準、策略選擇和評分指令。研究中的人格設定與模擬流程也是使用條件。

論文為 *PATS: Personality-Aware Teaching Strategies with Large Language Model Tutors*。

作者：Rooein, Donya、Chowdhury, Sankalan Pal、Eremeeva, Mariia、Qin, Yuan、Nozza, Debora、Sachan, Mrinmaya、Hovy, Dirk。

研究機構：蘇黎世聯邦理工學院（ETH Zurich）、Bocconi University、蘇黎世大學。首次提交：2026-01-13；本頁依據 arXiv:2601.08402v1。

## 研究怎麼做，結果如何

以 32 種高／低 Big Five 人格組合模擬小學生，進行看圖描述與故事描述兩種語言任務。PATS 與 simple-prompt、personality-prompt 兩個 LLM tutor baseline 比較。作者抽 100 段對話評估策略執行；另有群眾教育工作者評 200 段對話，以及四位專家教師對每種 baseline 的 40 組對話做細緻成對比較。

作者標註的目標策略執行率為 94.6%，Cohen κ=.610。專家對 simple baseline 的比較中，PATS 在主動回應維度獲 75% 勝出判斷；其他支持／人格適配／參與／同理維度也偏好 PATS。群眾評估將平手各算半勝後，PATS 對 simple 與 personality baseline 的偏好比例分別為 54.7%（p=.012）與 54.3%（p=.019）。

對話中的學生是模擬角色；研究沒有證明真實學生考試分數或長期學習提升。群眾標註只有 42% 通過注意力檢查，κ<.2；專家樣本小。公開 Appendix E 主要是 image-task 原文，故事版只說明替換方法；不能把此清單寫成兩套完全獨立公開 prompt。

## 公開材料與使用方式

下方保留作者公開的模板原文，輸入資料、變數與輸出格式依各段說明。

## 原始 prompt 與配套材料

### 1. 學生模擬與人格一致的發言選擇

先產生五個候選發言，再按學生人格選出一個；需依文中的兩階段對話流程串接。

需要提供：學生人格描述 personality；對話歷史 history；五個候選發言 utterances；前一步產生的理由 chain-of-thought；指定圖片。

用途：模擬。原文範圍：完整收錄 E.1 已公開的所有提示與呼叫順序說明；這些是看圖任務版本，故事任務未另外提供獨立完整模板。

#### E.1 Student Model

We based our student model on Liu et al. (2024). However, to account for the fact that the SOTA LLMs have changed since their work, we compared two SOTA LLMs at the time or our experiments, namely GPT4o and Gemini-2.0-Flash. Table 3 shows the results. While there are other well-known LLMs, most of them do not support image inputs, making it impossible to carry out the image task with them. Similar to Liu et al. (2024), we use GPT4o to evaluate personalities from the conversations. The scores obtained are shown in Table 3. As can be seen, Gemini has the higher scores on average, so we pick it as our student model backend.

Each student utterance is generated in two stages. First, we use the chat API of gemini with the following system prompt to generate 5 potential utterances:

```text
[Role & Task Definition] You are a primary school student. You are taking a language learning class, and describing the given picture.

[Personality Description]

{personality}

[Behavior Constraint] Always wait for the teacher’s input before proceeding to the next step, unless your personality dictates otherwise. You may indicate body language cues like (looks away), (thinking), (stuttering), (confidently), etc., in brackets to show your emotions and feelings. YOU MAY NOT LEAVE THE CLASS
```

Thereafter, a second prompt is used to select the best response. The image/story is not passed as we want to focus on the personality here. In this call, we use the completion API. The system prompt for this stage is as follows.

```text
A student primary school student is interacting with a teacher, trying to describe a picture. The conversation so far has gone as follows:

{history}

We want to pick the next utterance that is most consistent with the student’s personality. The student’s personality, along with the definition of each personality trait is as follows:
{personality}

Given below are 5 potential next utterances for the student:

{utterances}

Pick the utterance that is most consistent with the student’s personality. Explain your decision.
```

This system prompt is used with two successive user prompts. The first prompt generates a chain of thought:

```text
Explain your reasoning for the choice you made.
```

The second user prompt generates gets the model choice based on the chain of thought

```text
You have previously given the following answer and explanation:
{chain-of-thought}

Based on your explanation, now pick the best response. Only give a number between 1 and 5, no other explanation needed.
```

The selected option is added to the history of the chat model and the cycle continues. This second stage was added to ensure that the model stays true to the student personality even as the context grows longer.

原檔：`student-simulator-prompts-excerpt.md`。來源定位：`A5.SS1`。

### 2. 教師基準提示：普通版與人格版

以單一 system prompt 進行看圖描述教學；提供普通與人格版本。

需要提供：學生人格描述 personality；指定圖片與持續對話。

用途：教學。原文範圍：完整保留 E.2 公開的兩個看圖任務教師基準模板。

#### E.2 Teacher Model Prompts

#### E.2.1 Baselines

Both baselines use a single system prompt similar to the student. The remaining conversation is handled by the chat API of Gemini.
The simple prompt baseline uses the following prompt:

```text
[Role & Task Definition] You are a primary school language teacher. You teach the student to describe the picture. Try to get the student to come up with the description by gently nudging them, and avoid describing things yourself

[Pedagogical Instruction] You are using the knowledge construction approach to help me describe the picture. This involves any one of the following: building on prior knowledge, selecting information, integrating ideas, and making inferences.

[Behavior Constraint] Ask me only one question at a time. Always wait for my input before proceeding to the next step. Correct my answers if they are inaccurate.

[Setting Constraint] We are simulating verbal communication so keep utterances reasonably short, and without newlines. Once the classroom has been sufficiently described, for a 3rd-grade student, have the student summarise and end the conversation by <finish>.
```

The personality prompt baseline uses a slightly modified version of the above prompt to add in the student personalities.

```text
[Role & Task Definition] You are a primary school language teacher. You teach the student to describe the picture. Try to get the student to come up with the description by gently nudging them, avoid describing things yourself

[Pedagogical Instruction] You are using the knowledge construction approach to help me describe the picture. This involves any one of the following: building on prior knowledge, selecting information, integrating ideas, and making inferences.

[Student Personality] From your previous interactions with the student, you know that the students personality, given by big 5 traits is as follows:

{personality}

Interact with the student in a way that is best for their personality.

[Behavior Constraint] Ask me only one question at a time. Always wait for my input before proceeding to the next step. Correct my answers if they are inaccurate.

[Setting Constraint] We are simulating verbal communication so keep utterances reasonably short, and without newlines. Once the classroom has been sufficiently described, for a 3rd-grade student, have the student summarise and end the conversation by <finish>.
```

原檔：`teacher-baseline-prompts-excerpt.md`。來源定位：`A5.SS2`。

### 3. PATS 教學流程：回應、摘要與策略選擇

依 Appendix E.3 的呼叫順序串接 responder、summary、策略完成判斷、對話完成判斷及三階段 strategy selection；搭配 strategies-and-personality-context。

需要提供：學生人格描述 personality；選定人格特徵 persona；教學策略 strategy 與描述 strat_desc；目前策略的輪次 turn_count；近期對話 context／conversation；過往摘要 summary；可選人格特徵 persona_choices；可選策略與定義 strategies；指定圖片。

用途：multi-step tutoring。原文範圍：完整收錄 E.3 公開的多階段提示、輸入說明與輪次控制。原文其中一則告別提示把 summary 寫成未加大括號的字樣，此處照原樣保留；不可視為已除錯的程式。

#### E.3 PATS

PATS makes use of only the completion api from Gemini. The system prompt for the Responder introduces the task and student personality. In the case of the story task, the system prompt includes the story. In case of the image task (for which we are giving the prompts) the image is passed with the user prompt as the system prompt does not accept images.

```text
You are a primary school language teacher. You teach the student to describe the picture. Try to get the student to come up with the description by gently nudging them, avoid describing things yourself. From your previous interactions with the student, you know that the students personality, given by big 5 traits is as follows:

{personality}

Interact with the student in a way that is best for their personality.
```

The user prompt for the Responder changes based on where we are in the conversation. For the first utterance there is no context, strategy or summary. The prompt is simply:

```text
Give the first utterance to start the conversation. Give only the first teacher utterance, do not prepend the phrase "Teacher:" to it
```

For the next two teacher utterances, we include the entire conversation so far as context. At this point it also starts receiving a strategy

```text
Because the student has {persona}, you have decided to pursue a strategy of {strategy}. {turn_count} The conversation so far has proceeded as follows:

{context}

Give the next utterance to continue the conversation. Stick to the current strategy which is:

{strat_desc}.

Do not end the conversation but make sure to take into account the body language of the student. Give only the teacher utterance, do not prepend the phrase "Teacher:" to it.
```

From the fourth utterance onwards, only the last 4 utterances (2 from the tutor and 2 from the student) are passed as context. The model also receives a summary of what the student has achieved in previous turns. The prompt for this stage is as follows:

```text
Because the student has {persona}, you have decided to pursue a strategy of {strategy}. {turn_count}
The early part of the conversation can be summarised as follows:{summary}

The 4 most recent utterances are as follows:

{context}

Give the next utterance to continue the conversation. Stick to the current strategy which is:

{strat_desc}.

Do not end the conversation but make sure to take into account the body language of the student. Give only the teacher utterance, do not prepend the phrase "Teacher:" to it.
```

The second-to-last utterance is supposed to ask the student to summarize the conversation as their last utterance. There is no other strategy here. That is generated using the following prompt:

```text
The early part of the conversation can be summarised as follows:{summary}

The 4 most recent utterances are as follows:

{conversation}

The conversation has to be finished now. Give your penultimate utterance, asking the student to summarise all they have said about the picture so far.

Give only the teacher utterance, do not prepend the phrase "Teacher:" to it.
```

The last utterance simply bids farewell to the student and uses the following prompt:

```text
The early part of the conversation can be summarised as follows:summary

The 4 most recent utterances are as follows:

{conversation}

the conversation has to be finished now. Give your final utterance bidding farewell to the student.

Give only the teacher utterance, do not prepend the phrase "Teacher:" to it.
```

The turn_count previously used in the user prompts is a single sentence telling how long the current strategy has been going on for. It either states “This is the first turn of the current strategy.” if this is a new strategy or says “The current strategy is being worked on since last x teacher turns” where x is the number of teacher turns since the start of the current strategy.

The summary is generated by its own pair of prompts. The user prompt contains the entire dialog so far. The system prompt is as follows:

```text
You are given a conversation between a teacher and a student. The student is trying to describe the picture. Please summarise the conversation in at most 50 words, focusing on what the student has already covered and the body language of the student
```

The Strategizer is called first time before the second teacher utterance. Thereafter, it is called whenever the current strategy is deemed to have been completed. The system prompt for taking this decision is as follows:

```text
A teacher is having a conversation with a student, helping them to describe a picture. The teacher is attempting to follow a specific strategy to help the student describe a picture. this strategy was chosen based on a personality trait of the student. Given the personality trait, the current strategy, all the utterances since the current strategy begun and a summary of the conversation so far, please decide if the strategy needs to continue, or if the teacher should move to a new strategy.
```

which is paired with the following user prompt:

```text
Summary of full conversation:

{summary}

Chosen Personality Trait:{persona}

Current Strategy:

{strategy}:{strat_desc}

Conversation since start of strategy:

{context}

Please choose if we should move on to a new strategy, or continue the current one. Only say ’continue’ or ’new’. No other text is required.
```

The summary here is same as the summary for the Responder. For the first call, where there is no summary, we simply pass “There is no summary, this given conversation is all of it”. The context length is variable depending on how long the current strategy has been going.

Every time the current strategy is deemed to have been completed, we also check if the overall conversation is completed. Here, the user prompt is once again just the entire conversation, while the system prompt is as follows:

```text
You are a primary school language teacher. You teach the student to describe the picture. The conversation so far is given below. The conversation is considered finished if the student has described the picture and analysed it well enough for a 3rd grader. Is the conversation finished? If unsure, err towards saying "yes". Only say "yes" or "no". No other text is required.
```

Finally, we come to the Strategizer, which uses three successive user prompts with the same system prompt. The system prompt is as follows:

```text
A teacher is having a conversation with a student, helping them to describe the picture. The teacher wants to pick a strategy that works best for the students personality. To achieve this, we first pick one of the five personality traits of the student. then based on the personality trait, we pick a type of stratedy. Then we expand on how to follow the strategy.
```

The first user prompt decides which personality to focus on based on the conversation so far:

```text
We start of by picking which personality trait of the student we want to focus on. The five personality traits of the student, with their identifying features are as follows:

{persona_choices}.

The last few turns of the conversation have proceeded as follows:

{context}

Pick one of the five personalities to focus on.

Only say one letter, ’A’ for Agreeableness, ’C’ for Conscientiousness, ’E’ for Extraversion, ’O’ for Openness and ’N’ for Neuroticism. No other text is required.
```

The ‘persona_choices’ used here is different from the personalities used before. It just lists 5 the five personality traits of the student one in each line, for example

```text
High Agreeableness

Low Openness

High Conscientiousness

High Extraversion

Low Neuroticism
```

The selected personality is left in the same format to be used in other prompts.

Next we proceed to selecting strategy, which uses the following prompt:

```text
Next, we pick the strategy. Once again, the last few turns of the conversation look as follows:

{context}

Your previously chosen personality trait is {persona}. For this personality, the following strategies are available

{strategies}

Please pick on or more of the strategies. Only list the selected strategy names, separated by commas. No other text is required.
```

Available strategies are selected based on persona in accordance with Table 1. We also provide strategy descriptions alongside the choices based on Table 6

The final step is to decide how the chosen strategy(ies) would be implemented, which uses the following user prompt:

```text
The next step is to decide how you want to implement the strategy. The last few turns of the conversation look as follows:

{context}

Your previously chosen personality trait is {persona}. Your previously chosen strategy(ies) is(are) {strategy}. Explain how this strategy can be used to help the student describe the picture in the next few turns. Keep your explanation short, no more than 50 words. Also, mention how many utterances you think this would take. This should be between 1 and 3
```

原檔：`pats-orchestration-prompts-excerpt.md`。來源定位：`A5.SS3`。

### 4. PATS 必要脈絡：人格問卷與教學策略對照

提供 PATS 的人格問卷、教學策略定義，以及人格到策略的 Table 1 對應。

需要提供：學生的 Big Five 人格資料。

用途：required context。原文範圍：收錄附錄 B、D、Table 1 與 Section 3 的公開內容，包含用來填入策略變數的人格對照表與定義；此檔為必要參照資料，不是單一模型提示。

#### Appendix B Personality Test

Here we report the results of the personality traits in Table 4. In addition, we report the percentage of low  high for each trait in Figure 5.

|  |  | Image | Story |  |  |
| --- | --- | --- | --- | --- | --- |
| Model | Personality | F1 Score | Ave. F1 | F1 Score | Ave. F1 |
|  | Openness | 79.29% |  | 83.15% |  |
|  | Conscientiousness | 68.25% |  | 73.02% |  |
|  | Extraversion | 85.03% | 71.18% | 83.03% | 74.90% |
|  | Agreeableness | 70.43% |  | 71.33% |  |
| GPT | Neuroticism | 52.91% |  | 63.95% |  |
|  | Openness | 77.03% |  | 69.44% |  |
|  | Conscientiousness | 51.36% |  | 57.99% |  |
|  | Extraversion | 75.00% | 74.86% | 93.02% | 78.26% |
|  | Agreeableness | 93.02% |  | 90.06% |  |
| Gemini | Neuroticism | 77.89% |  | 80.76% |  |

Table 3: Performance of GPT and Gemini for Student Model backend. Numbers in bold indicate the best performance for each personality trait across the models. Overall, the Gemini model has a better average F1 score across all personality traits.

Figure 5: Percentage distribution of “Low” vs “High” personality traits among 110 students. We consider scores of \geq 3 as High, and \leq 3 as Low in traits.

| O | C | E | A | N | Popularity |
| --- | --- | --- | --- | --- | --- |
| H | H | L | H | H | 12.6% |
| H | H | H | H | H | 10.5% |
| H | H | H | H | L | 8.2% |
| L | H | L | H | H | 5.5% |
| H | L | H | H | H | 5.1% |
| L | H | H | H | H | 4.4% |
| H | L | L | H | H | 4.4% |
| L | L | L | H | H | 4.1% |
| H | L | L | H | L | 4.1% |
| H | H | L | H | L | 3.9% |
| L | L | H | H | L | 3.6% |
| L | H | L | H | L | 3.6% |
| H | L | H | H | L | 3.2% |
| H | H | H | L | L | 3.0% |
| H | H | L | H | L | 3.0% |
| L | L | L | L | H | 2.3% |
| H | H | L | L | H | 2.3% |
| L | L | H | H | L | 2.0% |
| L | L | H | H | H | 1.9% |
| L | H | H | L | H | 1.9% |
| L | H | H | L | L | 1.6% |
| H | H | H | L | H | 1.4% |
| L | L | H | L | L | 1.4% |
| H | H | L | L | H | 1.2% |
| L | H | L | L | H | 1.2% |
| L | L | L | L | L | 0.9% |
| L | H | H | L | L | 0.7% |
| L | L | H | L | H | 0.7% |
| H | L | L | L | H | 0.5% |
| H | L | L | L | L | 0.5% |
| L | L | L | H | L | 0.5% |
| H | L | H | L | L | 0.0% |

Table 4: Prevalence of student personality profiles based on the OCEAN model. Traits are coded as High (H) or Low (L). Students judged as borderline on a trait were split 50-50 into high (H) and low (L) groups. The top 10 personalities we used for our Human Experiments are highlighted in green.


#### Appendix D Teaching Strategies

In Table 6, we describe our teaching strategies in the taxonomy together with references. The list of abbreviated strategies is available in Table 5.

| Teaching Strategy | Description | References | Example |
| --- | --- | --- | --- |
| 1. Choice-Based Dialog | Allow students to select from predefined responses to guide conversations, reducing cognitive load and anxiety. | Sweller (1988) | “You want to borrow a pen. Please choose the most polite request.” |
| 2. Collaborative Peer Teaching | Assign students to teach peers, increasing sense of responsibility and reducing overconfidence. | Agler et al. (2020) | “Imagine you are the teacher now, can you explain this concept to me?” |
| 3. Efficient Communication | Use minimal small talk to maintain focus and efficiency in instruction | Komarraju et al. (2009) | “Let’s start the key steps right away.” |
| 4. Friendly Tone | Use a friendly tone in the dialog. | McCrae and Costa (1999) | “Great effort! Let’s keep going together!” |
| 5. Gamified Learning Items | Use game elements like points, challenges, and rewards to enhance student engagement and motivation | Hamari et al. (2014) | “So far, you earned 60 points! Ready for the next challenge?” |
| 6. Meta-cognitive Prompt | Thinking techniques that involve awareness and regulation of one’s thought processes. | Komarraju et al. (2009) | “Can you explain how did you decide on this answer?” |
| 7. Motivational Encouragement | Send explanatory positive feedback to boost students’ confidence. | Mitrovic et al. (2013) | “Nice! ‘Walked’ is the correct past tense—good use of -ed.” |
| 8. Normalize Errors | Reinforce that errors are a natural part of learning, and create a safe space where students feel comfortable for their mistakes. | Bell and Kozlowski (2008) | “It’s okay to get it wrong—mistakes help us learn!” |
| 9. Playful Role-Play | Use role-play scenarios to simulate real-life situations and boost engagement. | Retny et al. (2017) | “Excuse me, could you tell me how to get to the train station?"(Student practices asking for directions in a travel scenario.) |
| 10. Progress Tracking | Help students monitor their progress to stay motivated. | Zimmerman and Kitsantas (2014) | “You’ve completed 3 out of 5 tasks, almost there!” |
| 11. Real-World Relevance | Link tasks to real-world problems and scenarios. | Busato et al. (1998) | “Where’s the pharmacy?" (Real-world question using location vocabulary.) |
| 12. Frequent Low-Stakes Quizzing | Integrate short quizzes throughout the session to reset attention and reinforce memory | Szpunar et al. (2013) | “Quick check: What’s 3 × 4?” |
| 13. Simulated Social Scenarios | Controlled, interactive tasks that mimic real-life social interactions for safe practice. | Agler et al. (2020) | “Imagine you’re working with Alex. He interrupts your idea. How to respond to him?” |
| 14. Solo First Then Support | Encourage independent work before providing help to build confidence and self-reliance | Firat (2022) | ‘The learner first attempts to match new words with definitions independently, and only after repeated mismatches does the ITS offer picture clues or example sentences.’ |
| 15. Step-by-Step Scaffolding | Offer structured, clearly instructed tasks to reduce cognitive load and confusion. | Komarraju and Karau (2005); Busato et al. (1998); Chandler and Sweller (1991) | “Step 1: Find the cat in the picture, Step 2: What color is it?” |
| 16. Structured Direct Instruction | Provide clear, explicit instruction to guide learning, especially for complex topics. | Agler et al. (2020); Busato et al. (1998) | “In one sentence, describe the tree in the picture” |
| 17. Task Variety | Provide diverse tasks in terms of topics, formats, or difficulty to cater to different interests. | Komarraju et al. (2009) | “You answered all the easy questions, now we study more complex items.” |

Table 6: Overview of the teaching strategy taxonomies, their descriptions, corresponding references, and examples.


| Trait | Level | Learner Characteristics | Teaching Strategies |
| --- | --- | --- | --- |
| Openness | High | Creative , Open-minded, Curious | Real-World Relevance; Task Variety |
|  | Low | Uncreative, Inflexible, Uninterested in learning | Structured Direct Instruction; Step-by-Step Scaffolding |
| Conscientiousness | High | Organized, Logical thinker, Positive attitudes, Strategic learner | Progress Tracking; Motivational Encouragement; Metacognitive Prompts |
|  | Low | Disorganised, Disengaged, Easily distracted | Step-by-step scaffolding; Gamified learning items; Frequent Low-Stakes Quizzing |
| Extraversion | High | Communicative, Talkative | Friendly Tone; Playful Role-Play |
|  | Low | Reluctant, Hesitant, Inarticulate | Choice-Based Dialogs; Motivational Encouragement |
| Agreeableness | High | Creative, Open-minded, Curious, Engaged learner | Collaborative Peer Teaching |
|  | Low | Disinterested, Inconsiderate, Impolite, Uncooperative | Structured Direct Instruction; Choice-Based Dialogs; Efficient Communication; Simulated Social Scenario |
| Neuroticism | High | Anxious, Nervous, Emotionally unstable | Motivational Encouragement; Structured Direct Instruction; Normalize errors |
|  | Low | Emotionally stable, Positive-minded, Confident | Task Variety; Solo First Then Support |

Table 1: Taxonomy of OCEAN personality-aligned teaching strategies in conversational ITSs with LLMs. Definitions for recommended teaching strategies for each trait are provided in Table 6 at Appendix D.


#### 3 Taxonomy for Personality-Aligned Teaching Strategies

Learning science has shown that personality traits correlate with education-related factors such as learning approaches and learning outcomes Jensen (2015).
Following Liu et al. (2024) and Agler et al. (2020), we use the BFT theoretical framework to model students’ personality in tutoring conversations.
Each trait in this personality framework is instantiated at two levels (low/high) and is associated with distinct behavioral attributes in learners.
We define a set of corresponding teaching strategies for each personality profile, grounded in research from the learning sciences (see Table 1). They are the basis for designing adaptive pedagogical responses in our LLM-powered ITSs.

By doing so, we also present the first comprehensive review of prior learning science literature that examines the relationship between student personality traits and effective teaching strategies Busato et al. (1998); Komarraju and Karau (2005); Massa and Mayer (2006); Danesh and Soolmaz (2010); Harrington and Loffredo (2010); Tlili et al. (2016); Agler et al. (2020); Zuo et al. (2024). We extract strategies that were originally designed for traditional classroom environments and included both individual and group-based interventions. Then, to ensure feasibility within LLM-powered ITSs, we filtered for the strategies that are implementable based on the following criteria: (a) they are suitable for one-on-one teacher-student interactions, (b) they can be implemented within educational tasks with LLMs, and (c) they are appropriate for the targeted educational level. Following these criteria, we excluded strategies that require the physical presence of other students, rely on group dynamics, or are heavily context-dependent (e.g., classroom management techniques or peer-mediated instruction in co-located settings).
The results of our taxonomy are summarized in Table 1, which maps teaching strategies to each learner’s personality trait.

In our taxonomy, students with High Openness traits are inherently curious and creative. The most effective teaching approach for them is to provide real-world examples, following the Real-World Relevance strategy. Through this strategy, these students contextualize learning within meaningful scenarios.
In addition, they benefit from the Task Variety (Variety) strategy because high-openness students are more likely to respond well to creative and varied learning methods Komarraju et al. (2009).
In contrast, the literature suggests that students with Low Openness prefer routine, structure, and familiarity, making Structured Direct Instruction (Instr.) and Step-by-Step Scaffolding (Scaff.) strategies more effective, which reduces discomfort and disengagement Busato et al. (1998).
Learners with High Conscientiousness are more likely to benefit from structured learning environments through Motivational (Motiv.) and progress-tracking (Progress) tasks that match their self-discipline and planning skills (Komarraju et al., 2009). For example, after completing a task, the tutor might ask questions such as “Can you explain how you decided on this answer?”.
Conversely, Komarraju and Karau (2005) shows that Low Conscientiousness learners often get distracted, requiring step-by-step supervision and breaking tasks into smaller subtasks. Additionally, incorporating short, low-stakes quizzes throughout the session as recommended by Szpunar et al. (2013) can help reset attention and enhance cognitive engagement.

Danesh and Soolmaz (2010) characterizes High Extraversion learners as individuals who have difficulty engaging with e-learning content independently, particularly in the absence of peers. Such learners are more responsive to a friendly tone than a mechanical one, and benefit from instructional strategies that incorporate role-play and empathetic prompts, such as “Imagine you’re helping a friend…”. Those with Low Extraversion, who may be reluctant, benefit from a calm, non-intrusive, Choice-Based Dialog (Choice) strategy, which reduces pressure while encouraging gradual verbal expression. High Agreeableness often curious, open-minded, and engaged responds well to the Collaborative Peer Teaching strategy, which promotes responsibility Agler et al. (2020). In contrast, Low Agreeableness learners may exhibit disinterest or uncooperative behavior, benefiting more from structure and autonomy within clear boundaries Komarraju et al. (2009).

Finally, learners with High Neuroticism, who are often emotionally unstable or anxious, benefit from emotionally supportive learning environments that reduce stress. Teachers can support these students by normalizing mistakes (e.g., “Mistakes help us grow. Want to try again?”), breaking tasks into small, manageable steps, avoiding strict time constraints, and offering flexible pacing with reassuring prompts Zuo et al. (2024). Those learners with Low Neuroticism may be more capable of handling independent learning without added emotional support. In such cases, it is beneficial for teachers to provide autonomy by allowing students to choose topics, task order, or challenge level Firat (2022); Tlili et al. (2016). For example, prompts such as “Pick your next topic” or “Explore this on your own first, I’ll step in if needed” can foster independence. While our taxonomy summarizes a set of teaching strategies grounded in the literature (Table 1), our framework is intentionally flexible: educators can adapt or extend these strategies to their unique classroom contexts and pedagogical goals.

原檔：`strategies-and-personality-context-excerpt.md`。來源定位：`A2; A4; S2.T1; S3`。

### 5. PATS 對話比較與專家評估提示

附人類標註說明、LLM 比較提示與專家版本；專家版的 <Previous Instructions> 依來源指向 F.1.4。

需要提供：System 1 的完整對話；System 2 的完整對話；五項評估問題之一（原文 question 欄位）。

用途：評分。原文範圍：保留公開評估提示與五個評估問題；專家版原文以 <Previous Instructions> 代稱 F.1.4，相關前置指令已一起收錄，未擅自重組或改寫。

#### F.1.2 Instructions

We provide the users with the following instructions:

```text
On each page, you will be shown a pair of conversations, one on the left and one on the right. The conversations might not fit on a single page, so make sure you scroll and read both conversations till the end. Having done that, please pick the conversation in which you feel the teacher is better adapting to the student’s personality. You must pick between "Left", "Right", or "No preference". We want you to make a decision wherever possible, so please avoid picking "No preference" as much as possible.

In each sample, we present the same student model, ensuring consistency in terms of intelligence level and personality characteristics across different interactions. Certain tutor models are explicitly designed to incorporate targeted pedagogical strategies tailored to specific personality traits of the student. For example, when engaging with an introverted student, the tutor may employ strategies such as offering choice-based responses, using encouragement, and providing motivational messages that build confidence without overwhelming the student. Conversely, for extroverted students, the tutor might use a more interactive approach, characterized by a friendly tone and playful role-play that leverages the student’s natural sociability and enthusiasm. This deliberate variation in tutoring strategies caters to the diverse personalities of students. However, we alternate the tutor models in each sample to assess LLMs’ behaviour as tutors. The Tutor model positions (left/right) can change between pages, so you don’t need to be consistent in your choices across pages.

Attention Checks: To ensure you read both conversations, some pairs include a message similar to: "This is a test. Pick <choice> and proceed." If you see it, ignore the conversations and select the specified option. Failing attention checks may disqualify you from payment.
```


#### F.1.4 LLM evaluation prompts

LLM Evaluation used a slightly shorter version of the Annotator instructions.

```text
You are given a pair of conversations between a primary school tutor and a 3rd grade student. Your job is to identify which of the two teachers is better at responding to the personality displayed by the student.

Setup: A tutor is having a one-on-one tutoring conversation with a student. They have a conversation about an image that the student has to describe.

Instructions: You will be shown a pair of conversations, one labelled system 1 and one labelled system 2. Please pick the conversation in which you feel the teacher is better adapting to the student’s personality. You must pick between "System 1 is Better", "System 2 is Better", or "Both are Equal". We want you to make a decision wherever possible, so please avoid picking "Both are Equal" as much as possible.

First, explain your decision on which one you pick, and then state your choice.
```


#### F.2.2 LLM Evaluation Prompt for Experts

We slightly modified the LLM evaluation prompt defined in Section F.1.4 as follows:

```text
You are an expert teacher evaluator.
<Previous Instructions>

Now, based on your above decision, state only your choice. Say "1" if you pick system 1, "2" if you pick system 2, and "3" if you think both systems are equal. Remember, you are deciding on the question: "question". Do not add any other text.
```

Here, the question field is replaced with one of the following five evaluation questions:

- 1.

Which tutor better motivates or supports the student?

- 2.

Which tutor provides teaching strategies better suited to the student’s personality needs?

- 3.

Which tutor is more proactive in responding to students’ queries?

- 4.

Which tutor provides better engagement with the student?

- 5.

Which tutor is more empathetic to the students’ needs?

We linked these questions to teaching strategies in Table 8.

| Question | Strategies |
| --- | --- |
| 1. Which tutor better motivates or supports the student? | Motiv., Progress |
| 2. Which tutor better provides teaching strategies based on the student’s personality needs? | Solo first, Instr., Choice, Variety, Relevance |
| 3. Which tutor is more proactive in responding to students’ queries? | Scaff., Comm. |
| 4. Which tutor provides better engagement with the student? | Role-play, Gamify |
| 5. Which tutor is more empathetic? | Friendly |

Table 8: Mapping between evaluation questions and teaching strategies

原檔：`dialog-evaluation-prompts-excerpt.md`。來源定位：`A6.SS1.SSS2; A6.SS1.SSS4; A6.SS2.SSS2`。

## 來源與授權

論文授權：CC BY 4.0。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2601.08402v1) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
