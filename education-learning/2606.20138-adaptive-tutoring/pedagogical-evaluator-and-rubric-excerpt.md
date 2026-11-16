# Pedagogical evaluator, fourteen criteria and weights

Paper: Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring

Authors: Chang, Po-Chin; Hogan, Nicholas; Plaat, Aske; van der Meer, Michiel T.

Source: https://arxiv.org/html/2606.20138v2#A8

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Complete published evaluator/rubric/weight sections; the source JSON example itself abbreviates the feature keys as "... (14 features) ...", so this is not a fully specified machine-ready JSON schema.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix H LLM Evaluator Prompt and Pedagogical Labeling Guidelines

This appendix provides the complete evaluative framework used by the automated LLM-based evaluator. By analyzing the full dialogue trajectory, the evaluator is instructed to make binary decisions across 14 pedagogical criteria.

### H.1 Evaluator System Prompt

System Instruction: LLM Evaluator

```text
You are an expert educational conversation evaluator. Using the guidelines provided in the next section, evaluate the following chat transcript.

For each criterion, think step by step and make a binary True/False decision based only on clear evidence in the transcript. If the criterion cannot be confirmed confidently, mark it as False. Do not infer user intent or emotion that is not explicitly expressed.

Return ONLY a JSON object with True/False for each criterion:
{
"answer_2_questions": boolean,
... (14 features) ...
}

### Dialogue Trajectory:
[Full Transcript]
```

### H.2 Labeling Guidelines (14 Criteria)

The following rubrics define the classification boundaries for the LLM evaluator to ensure objective pedagogical marking:

- 1.

Answer \geq 2 questions: The user answers two or more questions posed by the assistant about the main topic. (False if fewer than two or off-topic).

- 2.

Ask \geq 2 on-topic questions: The user asks two or more questions (why, how, what, when) connected to the topic. (Exclude generic greetings).

- 3.

Interact > 3 times: The user sends four or more substantive messages containing reasoning or topic-related inquiry.

- 4.

Positive social exchanges: The user expresses positivity (e.g., “thank you”, emojis) at least twice.

- 5.

Answers mostly correct: The user’s responses align with explanations in most cases with few clear mistakes.

- 6.

Correct within 2 turns: The user provides a correct response within two attempts at least 75% of the time when prompted.

- 7.

Shows understanding: Relevant responses and follow-up questions demonstrate comprehension without repeated confusion.

- 8.

Shows curiosity: Asks at least one question that goes beyond basic requirements (explores “why” or “how”).

- 9.

Justifies mistakes: After an error, the user either reflects on the reasoning or provides a corrected answer later.

- 10.

Assistant on topic: The assistant remains focused on the learning goal throughout the interaction.

- 11.

Assistant scaffolding: The tutor offers progressive, multi-turn guidance and adjusts help level when the student struggles. (False if gives full answers immediately).

- 12.

Assistant diagnoses: The assistant identifies specific mistakes and provides tailored clarifications.

- 13.

Assistant balances: The assistant alternates between explaining and prompting, avoiding a monologue-style delivery.

- 14.

Assistant adapts: The tutor changes behavior (e.g., more explanation after mistakes) based on student performance.


## Appendix I Pedagogical Criteria Weighting

To ensure the AI feedback signal aligns with human pedagogical judgment, we correlated the 14 LLM-extracted features against an expert-labeled dataset (N=138). Human experts evaluated sessions and label it to 0, 0.5, and 1. We then calculated the Pearson correlation coefficient between each binary LLM feature and the human-assigned scores to derive the empirical weights (\omega_{i}) shown in Table 4.

Table 4: Empirical weights derived from correlation analysis between LLM-extracted features and human expert labels.

| Feature Criterion (f_{i}) | Weight (\rho) |
| --- | --- |
| Student-Side Metrics (Engagement & Performance) |  |
| Justifies mistakes | 0.436 |
| Answers mostly correct | 0.387 |
| Answer \geq 2 questions | 0.368 |
| Interacts > 3 times | 0.315 |
| Correct within 2 turns | 0.215 |
| Shows understanding | 0.150 |
| Ask \geq 2 on-topic questions | -0.016 |
| Shows curiosity | -0.161 |
| Tutor-Side Metrics (Instructional Strategy) |  |
| Assistant provides scaffolding | 0.341 |
| Assistant adapts to the student’s level | 0.295 |
| Assistant diagnoses misunderstanding | 0.248 |
| Assistant balances explanation and questioning | 0.207 |
| Assistant stays on topic | 0.144 |
| Positive social exchanges | 0.008 |
