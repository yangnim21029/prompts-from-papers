# Human evaluation instructions

Source: https://arxiv.org/html/2603.08127v2#A3
Locator: Appendix C; Figure 9
License: CC BY 4.0
Extraction: 用 LiteParse 擷取 Figure 9 文字；移除頁首與圖說，保留原文與 PDF 換行。

---

You’ll be presented with a series of questions (research goals). For each question, two
 answers will be provided. Your task is to read both answers carefully and decide which one
 you believe is better.

 When judging, consider:

 Clarity: It examines whether the answer is clear and actionable (not just well-written), with
 concrete steps/mechanisms rather than vague jargon.
 Novelty: It examines whether the answer proposes a non-obvious idea or framework (new
 combinations/frameworks typically count more than swapping a single component).
 Feasibility: It examines whether the answer is a rigorous, testable research proposal (clear
 hypothesis→method→outcome chain, experiments/baselines/ablations, realistic resources,
 risk awareness). Do not penalize uncertainty or use of novel methods by itself.
 Relevance: It examines whether the answer matches the research goal’s core problem
 domain, required mechanisms, and required scope (general framework vs specific
 application).

 Question:
 {question}

 Answer A:
 {answer_a}

 Answer B:
 {answer_b}

 Based on the question, comparing these two answers, in terms of clarity, novelty, feasibility,
 and relevance, respectively.
 Give the win-tie-lose of Answer A compared to Answer B in each of the four aspects.

 Definitions (A compared to B):
 - win: Answer A is better than Answer B on this aspect.
 - tie: Answer A and Answer B are roughly equal on this aspect.
 - lose: Answer A is worse than Answer B on this aspect.

 Output (no extra text):
 Clarity: win/tie/lose
 Novelty: win/tie/lose
 Feasibility: win/tie/lose
 Relevance: win/tie/lose
