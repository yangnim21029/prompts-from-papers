# actor-refinement-without-history

Source: https://github.com/xand-stapleton/ai_agents/blob/8bae8219959d4e8ae1085694e5629a423bcf64ac/blocks/actor.py
Locator: blocks/actor.py: build_refinement_prompt, lines 95–99
License: GPL-2.0
Extraction: 以 Python AST 靜態讀取字串與 f-string，未執行來源程式；將變數插值保留為 {name}。Critic 的錯誤分類依原 ERROR_TYPES 完整展開；其餘原文未改寫。

---

You previously answered:
{previous_answer}

The critic feedback was:
{critic_feedback}

Revise the solution accordingly. Provide a clear final answer.
