# Dialog comparison instructions and LLM evaluation prompts

Paper: PATS: Personality-Aware Teaching Strategies with Large Language Model Tutors

Authors: Rooein, Donya; Chowdhury, Sankalan Pal; Eremeeva, Mariia; Qin, Yuan; Nozza, Debora; Sachan, Mrinmaya; Hovy, Dirk

Source: https://arxiv.org/html/2601.08402v1#A6.SS1.SSS2

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Published evaluation prompts and five questions; the source itself uses <Previous Instructions> rather than repeating the preceding prompt.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

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
