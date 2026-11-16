# Idea Direction Evolution

Source: https://arxiv.org/html/2603.08127v2#A4
Locator: Appendix D; Figure 10
License: CC BY 4.0
Extraction: 用 LiteParse 擷取 Figure 10 文字；移除頁首與圖說，保留原文與 PDF 換行。

---

# Role
You are an expert Machine Learning Research Engineer specialized in scientific idea
summarization and technical writing for persistent memory.

# Task
I will provide you with a user goal, a set of top-ranked candidate ideas (with ratings and
refinement feedback), and optional task outcomes.

Your goal is to distill reusable, goal-relevant **promising research directions** into a
compact memory item that can be retrieved in future tasks.

# Input Data
- **User Goal:** {user_goal}
- **Top-Ranked Ideas:** {top_ranked_ideas}
- Each idea may include: method sketch, experimental plan, key assumptions, and
reviewer feedback.

# Instructions
1. **DIRECTION SUMMARY**: Extract promising directions from top ranked ideas. For
each direction, include:
  - A clear direction title (one line).
  - The core mechanism or hypothesis.
  - Why it is promising for user goal (novelty/feasibility/relevance/clarity).
  - Key requirements and assumptions (data, compute, tools, environment).
  - A minimal experimental plan that could validate the direction (2–4 steps).
2. **DEDUPLICATION**: If multiple ideas express the same direction, merge them and
retain only the most actionable formulation.

# Constraints
- **Be Precise**: Do not omit concrete assumptions, evaluation signals, or experimental
steps.
- **Be Concise**: Use technical language. Avoid conversational filler.
- **Actionable Memory**: Write so a future researcher agent can directly reuse the direction.

# Output Format
DIRECTION SUMMARY:
- Direction 1: [Title]
 - Core idea:
 - Why promising for user goal:
 - Requirements/assumptions:
 - Minimal validation plan:
- Direction 2: ...
