# Meaningful code submission counter

Paper: Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning

Authors: Chung, Angel Tsai-Hsuan; Zhang, Botong; Kung, Ling-Chieh; Bastani, Hamsa; Bastani, Osbert

Source: https://arxiv.org/html/2608.16907v1#A2.F14

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Complete published Figure 14 task prompt.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

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
