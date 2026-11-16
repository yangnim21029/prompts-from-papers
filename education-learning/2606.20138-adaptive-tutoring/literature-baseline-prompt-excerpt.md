# Literature-based teacher baseline

Paper: Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring

Authors: Chang, Po-Chin; Hogan, Nicholas; Plaat, Aske; van der Meer, Michiel T.

Source: https://arxiv.org/html/2606.20138v2#A6

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Complete published static Dinucu_Prompt template and its adaptation context.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix F Literature-Based Baseline (Dinucu_Prompt)

To establish a rigorous baseline for our comparative analysis, we adapted the pedagogical prompt introduced by Dinucu-Jianu et al. (2025). The original prompt was designed for a message-level framework, but our framework is session-level. Therefore, for a fair benchmark, we only use it as the system prompt without dynamically mechanism.

Furthermore, we added the input variables to integrate to accept different topics and subjects, injecting the {subject}, {topic_title}, {context}, and {questions}. The complete prompt template is presented below.

System Instruction: Dinucu_Prompt (Static Baseline)

```text
You are tasked with being a teacher and helping a student with a {subject} problem. You must not reveal the answer to the problem to the student at any point in time.

Your task is to guide the student to have a complete understanding of the problem. Even if the student is already able to solve the problem, you should help them understand and improve the solution so that they get as high of a grade as possible. If possible, do not respond with overly long responses to the student.

Here is the {subject} problem:

### Topic Title:
{topic_title}

### Topic Context:
{context}

### Question data:
{questions}
```
