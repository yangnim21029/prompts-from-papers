# Student simulator and personality-consistent response selection

Paper: PATS: Personality-Aware Teaching Strategies with Large Language Model Tutors

Authors: Rooein, Donya; Chowdhury, Sankalan Pal; Eremeeva, Mariia; Qin, Yuan; Nozza, Debora; Sachan, Mrinmaya; Hovy, Dirk

Source: https://arxiv.org/html/2601.08402v1#A5.SS1

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — All published E.1 prompts and surrounding orchestration instructions; image-task versions, not independently supplied story-task templates.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

### E.1 Student Model

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
