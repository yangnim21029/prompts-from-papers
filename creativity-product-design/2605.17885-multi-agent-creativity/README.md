# 多代理創意發想：產生、討論與篩選點子

官方模板包含替代用途任務、六種實際問題，以及獨立發想、看過他人提案再發想、互評、討論與選擇等模式。先選任務，再選一套討論流程；各模式是實驗條件，不需要全部依序執行。

論文為 *Multi-agent AI systems outperform human teams in creativity*。

作者：Tiancheng Hu、Yixuan Jiang、Haotian Li、José Hernández-Orallo、Xing Xie、Nigel Collier、David Stillwell、Luning Sun。

研究機構：University of Cambridge、Zhejiang University、Microsoft Research Asia、Universitat Politècnica de València。首次提交：2026-05-18；本頁依據 arXiv:2605.17885v1。

## 研究怎麼做，結果如何

比較 71 個實驗條件、六種問題的 4,541 個多代理創意與 341 個人類團隊創意；人類為 114 個三人或六人團隊，另有 179 個單代理創意作參考。五位人類評分者在不知來源的條件下評新穎性與實用性；分數在任務內標準化後相乘為創意。評分前所有人類與 AI 創意都經 GPT-4.1 統一文風。另以語意向量分析討論軌跡。

多代理整體創意平均 0.297，人類團隊 0.151，Cohen’s d=1.50，p<.001。

優勢主要來自新穎性（d=1.29）；實用性差異小且不顯著（d=0.08，p=.14）。

模型選擇與討論結構合計解釋 26.8% 的 LLM 討論動態變異；persona 操弄與增加人數未構成普遍的創意提升保證。

這是 AI 團隊與人類團隊的比較，沒有直接測試人機混合團隊。

創意定義與任務限於文字問題解決；不能直接推論藝術、美學或科學突破。

評分前以同一 AI 改寫所有提案，且不同模型／討論流程匯總為主要效果；單一 prompt 本身的獨立效果未被識別。

官方 generation 程式仍使用 creative 名稱，README 說明它對應論文後來命名的 progressive 條件。

## 公開材料與使用方式

任務、討論、評分、角色與統一文風的原始材料依官方 CC BY-NC-SA 4.0 保存。原始常數集合與分拆模板有重複，不能按檔案數當成獨立方法數。論文 PDF 僅提供 arXiv 來源。

先讀 upstream/generation/prompts.py 的 TASK_REQUIREMENTS 映射，再將任務與所選階段組合；保留原提示的字數／排序格式。

## 原始 prompt 與配套材料

### 1. AUT_MODE1_OVERALL

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: You are collaborating with other team members to come up with five unusual uses of a rope.
Your ideas will be evaluated on their creativity (i.e., they should be both novel and useful).
```

原檔：`prompts/aut_mode1_overall.txt`。來源定位：`generation/prompts.py:4-7`。

### 2. AUT_MODE1_IDEA_GENERATION

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please propose 5 unusual uses of a rope.
- Each idea should be within 20 words and should not include explanation.
- List each idea on a separate line.
```

原檔：`prompts/aut_mode1_idea_generation.txt`。來源定位：`generation/prompts.py:9-13`。

### 3. AUT_MODE1_IDEA_GENERATION_DEPENDENT

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please propose 5 additional unusual uses of a rope that are different from the previous ideas.
- Each idea should be within 20 words and should not include explanation.
- List each idea on a separate line.
```

原檔：`prompts/aut_mode1_idea_generation_dependent.txt`。來源定位：`generation/prompts.py:15-19`。

### 4. AUT_MODE1_SELECTION_RATING

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- Below is the list of all proposed ideas.
- Please rate **each and every idea** on its creativity (i.e., novelty and usefulness), using a scale from 1 to 10. 
- Avoid giving the same score to multiple ideas unless absolutely necessary. 
- Provide your scores in the format 'Idea X: Y'.
- Ensure that the scores span a wide range to reflect varying levels of creativity.
```

原檔：`prompts/aut_mode1_selection_rating.txt`。來源定位：`generation/prompts.py:21-27`。

### 5. AUT_MODE1_SELECTION_SELECTIONTOP

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please review all the ideas listed below.
- Select 5 ideas that you find the most creative (i.e., novel and useful).
- List the idea numbers of your selections (each on a new line).
```

原檔：`prompts/aut_mode1_selection_selectiontop.txt`。來源定位：`generation/prompts.py:29-33`。

### 6. AUT_MODE1_DISCUSSION_RATING_ALLATONCE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- You are reviewing the current list of top ideas. Each idea should be evaluated individually.
- Your team has a maximum of 20 rounds to finalize the list of ideas. You are currently on round {{total_resp}}.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from the shared replacement pool of top ideas. Use this format:
    "Replace: [full replacement idea] - Reason: [why the old idea is not creative or not aligned with the task objective and the full replacement idea can be better]."

- **Guidelines for Reviewing the List**:
  1. Carefully evaluate each idea in the list based on the task objective.
  2. Do not summarize or output a final revised list. Focus only on evaluating individual ideas.
  3. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of 20 rounds** for your team. If you disapprove one idea, prioritise improving it over replacing it.
  4. Be concise: Each idea should be **within 20 words**.
  5. Focus on meaningful improvement or replacement that enhances alignment with the task objective.
```

原檔：`prompts/aut_mode1_discussion_rating_allatonce.txt`。來源定位：`generation/prompts.py:35-52`。

### 7. AUT_MODE1_DISCUSSION_SELECTIONTOP_ALLATONCE_FIRSTAGENT

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current list of top ideas. Each idea should be evaluated individually.
- Your team has a maximum of 20 rounds to finalize the list of ideas. You are currently on round {{total_resp}}.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."

- **Guidelines for Reviewing the List**:
  1. Carefully evaluate each idea in the list based on the task objective.
  2. Do not summarize or output a final revised list. Focus only on evaluating individual ideas.
  3. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of 20 rounds** for your team.
  4. Be concise: Each idea should be **within 20 words**.
  5. Focus on meaningful improvement that enhances alignment with the task objective.
```

原檔：`prompts/aut_mode1_discussion_selectiontop_allatonce_firstagent.txt`。來源定位：`generation/prompts.py:55-70`。

### 8. AUT_MODE1_DISCUSSION_SELECTIONTOP_ALLATONCE_OTHERAGENTS

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current list of top ideas. Each idea should be evaluated individually.
- Your team has a maximum of 20 rounds to finalize the list of ideas. You are currently on round {{total_resp}}.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from the replacement pool of top ideas selected by yourself. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
```

原檔：`prompts/aut_mode1_discussion_selectiontop_allatonce_otheragents.txt`。來源定位：`generation/prompts.py:72-82`。

### 9. AUT_MODE1_DISCUSSION_RATING_ONEBYONE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- Currently, you are discussing Idea #{{idea_index}}.
- This is discussion round {{current_round}} out of a total of {{max_rounds}} rounds for this idea.
- Please be mindful that your team has limited rounds to finalize this idea.

- Actions you can take for the current idea: 
  - **Agree**: If the current idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify**: If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace**: If the idea is not creative or not aligned with the task objective, replace it with one from the shared replacement pool of top ideas. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."

- Additional Guidelines:
  1. Be concise: Each idea should be **within 20 words**.
  2. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of {{max_rounds}} rounds** for your team. If you disapprove one idea, prioritise improving it over replacing it.
  3. Focus on meaningful improvement or replacement that enhances alignment with the task objective.
```

原檔：`prompts/aut_mode1_discussion_rating_onebyone.txt`。來源定位：`generation/prompts.py:85-101`。

### 10. AUT_MODE1_DISCUSSION_SELECTIONTOP_ONEBYONE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Currently, you are discussing Idea #{{idea_index}}.
- This is discussion round {{current_round}} out of a total of {{max_rounds}} rounds for this idea.
- Please be mindful that your team has limited rounds to finalize this idea.

- Actions you can take for the current idea: 
  - **Agree**: If the current idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify**: If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace**: If the idea is not creative or not aligned with the task objective, replace it with one from the replacement pool of top ideas selected by yourself. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."

- Additional Guidelines:
  1. Be concise: Each idea should be **within 20 words**.
  2. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of {{max_rounds}} rounds** for your team. If you disapprove one idea, prioritise improving it over replacing it.
  3. Focus on meaningful improvement or replacement that enhances alignment with the task objective.
```

原檔：`prompts/aut_mode1_discussion_selectiontop_onebyone.txt`。來源定位：`generation/prompts.py:103-119`。

### 11. PS_QUESTIONS/plastic_waste

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: Plastic waste is one of the biggest environmental problems of our lifetime. You are collaborating with other team members to come up with one creative idea to reduce plastic pollution.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-plastic_waste.txt`。來源定位：`generation/prompts.py:122-146`。

### 12. PS_QUESTIONS/supply_chain

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: Vulnerabilities within a supply chain could lead to uncontrolled costs and inefficient delivery schedules. You are collaborating with other team members to come up with one creative idea to tackle supply chain security.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-supply_chain.txt`。來源定位：`generation/prompts.py:122-146`。

### 13. PS_QUESTIONS/sorry_pandemic

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: Imagine a new pandemic has emerged that is transmitted by saying the word "sorry". You are collaborating with other team members to come up with one creative idea to reduce its spread.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-sorry_pandemic.txt`。來源定位：`generation/prompts.py:122-146`。

### 14. PS_QUESTIONS/education_inequality

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: Educational inequality is the unequal distribution of academic resources to disadvantaged and marginalised groups. You are collaborating with other team members to come up with one creative idea to overcome inequality in education.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-education_inequality.txt`。來源定位：`generation/prompts.py:122-146`。

### 15. PS_QUESTIONS/employee_attrition

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text

Task: Voluntary attrition happens when an employee decides to leave the company, resulting in the reduction of valued talent in the workforce. You are collaborating with other team members to come up with one creative idea to improve access to stop voluntary employee attrition.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-employee_attrition.txt`。來源定位：`generation/prompts.py:122-146`。

### 16. PS_QUESTIONS/singing_shower

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：任務指示。原文範圍：完整字串常數。

```text
Task: Imagine a new research study discovers that singing in the shower for 20 minutes or more is good for health. You are collaborating with other team members to come up with one creative idea to encourage people to do this.
The idea will be evaluated on its creativity (i.e., it should be both novel and useful).
```

原檔：`prompts/ps_questions-singing_shower.txt`。來源定位：`generation/prompts.py:122-146`。

### 17. PS_GENERATION

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please propose 5 possible ideas for the problem.
- Each idea should be around 80-100 words.
- Please return only the ideas, each on a separate line.
- Do not include any explanations or use markdown formatting. Do not add numbering to the ideas.
```

原檔：`prompts/ps_generation.txt`。來源定位：`generation/prompts.py:149-154`。

### 18. PS_GENERATION_DEPENDENT

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please propose 5 additional ideas for the problem that are different from the previous ideas.
- Each idea should be around 80-100 words.
- Please return only the ideas, each on a separate line.
- Do not include any explanations or use markdown formatting. Do not add numbering to the ideas.
```

原檔：`prompts/ps_generation_dependent.txt`。來源定位：`generation/prompts.py:156-161`。

### 19. PS_SELECTION_RATING

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- Below is the **EXACT and ONLY** list of ideas you are to rate. Do not add, remove, or modify any ideas in this list.
- Please rate **each and every idea** on its **creativity**, using an integer scale from 1 (Very Low Creativity) to 10 (Exceptional Creativity). 
- We define creativity as a combination of novelty (how original or unexpected the idea is in this context) and usefulness (its potential practical value or impact in addressing the goal). Consider both aspects when assigning your score
**Critically evaluate and differentiate** between the ideas. Assign unique scores wherever possible. Only assign the same score if two ideas are genuinely indistinguishable in their level of creativity based on the definition above.
Ensure your final scores span a wide range across the 1-10 scale (e.g., the difference between the highest and lowest score should be at least 5 points, if the ideas' quality allows for such differentiation). Do not cluster scores narrowly.
Provide **ONLY** your scores. **Strictly adhere** to the format 'Idea X: Y', with each score on a new line. Do **not** include any explanations, justifications, summaries, or any other text before or after the list of scores.
```

原檔：`prompts/ps_selection_rating.txt`。來源定位：`generation/prompts.py:163-170`。

### 20. PS_SELECTION_RATING_NOVELTY

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- Below is the **EXACT and ONLY** list of ideas you are to rate. Do not add, remove, or modify any ideas in this list.
- Please rate **each and every idea** on its **novelty**, using an integer scale from 1 (Very Low Novelty) to 10 (Exceptional Novelty). 
**Critically evaluate and differentiate** between the ideas. Assign unique scores wherever possible. Only assign the same score if two ideas are genuinely indistinguishable in their level of novelty.
Ensure your final scores span a wide range across the 1-10 scale (e.g., the difference between the highest and lowest score should be at least 5 points, if the ideas' quality allows for such differentiation). Do not cluster scores narrowly.
Provide **ONLY** your scores. **Strictly adhere** to the format 'Idea X: Y', with each score on a new line. Do **not** include any explanations, justifications, summaries, or any other text before or after the list of scores.
```

原檔：`prompts/ps_selection_rating_novelty.txt`。來源定位：`generation/prompts.py:174-180`。

### 21. PS_SELECTION_SELECTIONTOP

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please review all the ideas listed below.
- Select 3 ideas that you find the most creative (i.e., novel and useful).
- List the idea numbers of your selections (each on a new line).
```

原檔：`prompts/ps_selection_selectiontop.txt`。來源定位：`generation/prompts.py:181-185`。

### 22. PS_DISCUSSION_RATING

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- You are reviewing the current top idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for the idea:
  - **Agree:** If the current idea is extremely creative and you cannot come up with a more creative idea, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from **Replacement Ideas Pool:**. If the replacement pool is empty, this action is not allowed. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_discussion_rating.txt`。來源定位：`generation/prompts.py:187-200`。

### 23. PS_DISCUSSION_RATING_PRE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- You are reviewing the current top idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from **Replacement Ideas Pool:**. If the replacement pool is empty, this action is not allowed. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_discussion_rating_pre.txt`。來源定位：`generation/prompts.py:203-216`。

### 24. PS_DISCUSSION_SELECTIONTOP

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current list of top ideas.
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for the idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from the replacement pool of top ideas selected by yourself. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- Each idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_discussion_selectiontop.txt`。來源定位：`generation/prompts.py:218-231`。

### 25. PS_DISCUSSION_SELECTIONTOP_PRE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current list of top ideas.
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it with one from the replacement pool of top ideas selected by yourself. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- Each idea should be around 80-100 words.
```

原檔：`prompts/ps_discussion_selectiontop_pre.txt`。來源定位：`generation/prompts.py:234-246`。

### 26. PS_DISCUSSION_RATING_NoPool

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

- You are reviewing the current top idea.
- Your team has a maximum of {{max_rounds}} rounds to finalize the idea. You are on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for the idea:
  - **Agree:** If the current idea is extremely creative and you cannot come up with a more creative idea, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it by coming up with a new one of your own. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_discussion_rating_nopool.txt`。來源定位：`generation/prompts.py:248-261`。

### 27. PS_DIRECT_DISCUSSION_ALL_AT_ONCE_NoPool

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current idea.
- Your team has a maximum of {{max_rounds}} rounds to finalize the idea. You are on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for the idea:
  - **Agree:** If the current idea is extremely creative and you cannot come up with a more creative idea, reply "Agree: No changes needed."
  - **Modify:** If the idea shows a creative promise but requires a major overhaul, modify the idea such that it is significantly improved in terms of creativity. Do NOT simply polish it or add small elements. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, replace it by coming up with a new one of your own, a more creative one. Be bold, especially in earlier rounds. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.  
- Do not include word counts in your response.
```

原檔：`prompts/ps_direct_discussion_all_at_once_nopool.txt`。來源定位：`generation/prompts.py:263-276`。

### 28. AUT_DIRECT_FIRST_ROUND_ALL_AT_ONCE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are initiating the discussion for a collaborative task. Please propose 5 unusual uses of a rope.
- Each idea should be within 20 words and should not include explanation.
- List each idea on a separate line.
```

原檔：`prompts/aut_direct_first_round_all_at_once.txt`。來源定位：`generation/prompts.py:280-284`。

### 29. AUT_DIRECT_DISCUSSION_ALL_AT_ONCE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current list of ideas. 
- Your team has a maximum of 30 rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- The goal is to generate the SINGLE MOST CREATIVE idea, not to continually expand one idea.

- Actions you can take for each idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."

- **Guidelines**:
  1. Carefully evaluate each idea in the list based on the task objective.
  2. Do not summarize or output a final revised list. Focus only on evaluating individual ideas. 
  3. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of 30 rounds** for your team. If you disapprove one idea, prioritise improving it over replacing it.
  4. Be concise: Each idea should be **within 20 words**.
  5. Focus on meaningful improvement or replacement that enhances alignment with the task objective.
```

原檔：`prompts/aut_direct_discussion_all_at_once.txt`。來源定位：`generation/prompts.py:286-304`。

### 30. AUT_DIRECT_FIRST_ROUND_ONE_BY_ONE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are initiating the discussion for a collaborative task. Please propose an unusual uses of a rope.
- The idea should be within 20 words and should not include explanations.
```

原檔：`prompts/aut_direct_first_round_one_by_one.txt`。來源定位：`generation/prompts.py:306-309`。

### 31. AUT_DIRECT_DISCUSSION_ONE_BY_ONE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Currently, you are discussing Idea #{{idea_index}}.
- This is discussion round {{current_round}} out of a total of 15 rounds for this idea.
- Please be mindful that your team has limited rounds to finalize this idea.

- Actions you can take for the current idea: 
  - **Agree**: If the current idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify**: If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace**: If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."

- **Guidelines**:
  1. Be concise: Each idea should be **within 20 words**.
  2. Avoid unnecessary changes: While you can suggest improvement or replacement, keep in mind that there are **a maximum of 15 rounds** for your team. If you disapprove one idea, prioritise improving it over replacing it.
  3. Focus on meaningful improvement or replacement that enhances alignment with the task objective.
```

原檔：`prompts/aut_direct_discussion_one_by_one.txt`。來源定位：`generation/prompts.py:311-327`。

### 32. PS_DIRECT_FIRST_ROUND_ALL_AT_ONCE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Please propose one possible idea for the problem.
- The idea should be around 80-100 words.
- Please return only the idea.
- Do not include any explanations or use markdown formatting.
```

原檔：`prompts/ps_direct_first_round_all_at_once.txt`。來源定位：`generation/prompts.py:329-334`。

### 33. PS_DIRECT_DISCUSSION_ALL_AT_ONCE_Pre

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- Please be mindful that your team has limited rounds to finalize the idea.

- Actions you can take for the idea:
  - **Agree:** If the idea meets the task objective and does not require changes, reply "Agree: No changes needed."
  - **Modify:** If the idea is aligned with the task objective but needs improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_direct_discussion_all_at_once_pre.txt`。來源定位：`generation/prompts.py:336-349`。

### 34. PS_DIRECT_DISCUSSION_ALL_AT_ONCE

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- Please be mindful that your team has limited rounds to finalize the idea.

- Actions you can take for the idea:
  - **Agree:** If the current idea is extremely creative and you cannot come up with a more creative idea, reply "Agree: No changes needed."
  - **Modify:** If the idea is moderately creative and could use improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_direct_discussion_all_at_once.txt`。來源定位：`generation/prompts.py:351-364`。

### 35. PS_DIRECT_DISCUSSION_ALL_AT_ONCE_RESTRICTION_FIRST

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- Please be mindful that your team has limited rounds to finalize the idea.

- Actions you can take for the idea:
  - **Modify:** If the idea is moderately creative and could use improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_direct_discussion_all_at_once_restriction_first.txt`。來源定位：`generation/prompts.py:366-378`。

### 36. PS_DIRECT_DISCUSSION_ALL_AT_ONCE_RESTRICTION_OTHER

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You are reviewing the current idea. 
- Your team has a maximum of {{max_rounds}} rounds to finalize the list of ideas. You are currently on round {{total_resp}}.
- Please be mindful that your team has limited rounds to finalize the idea.

- Actions you can take for the idea:
  - **Agree:** If the current idea is extremely creative and you cannot come up with a more creative idea, reply "Agree: No changes needed."
  - **Modify:** If the idea is moderately creative and could use improvement, propose modification. Use this format:
    "Modify: [full idea after modification] - Reason: [specific reason for improvement]."
  - **Replace:** If the idea is not creative or not aligned with the task objective, propose a new idea to replace the current one. Use this format:
    "Replace: [full replacement idea] - Reason: [specific reason for replacement]."
- The idea should be around 80-100 words.
- Do not include word counts in your response.
```

原檔：`prompts/ps_direct_discussion_all_at_once_restriction_other.txt`。來源定位：`generation/prompts.py:380-393`。

### 37. CREATIVE_IDEA_GENERATION

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- You have a ranked list of current ideas.
- The goal is to generate exactly five radically NOVEL ideas, inspired by, but NOT simply a combination of, the existing ideas.
- Think *transformatively*.  What fundamental shifts in approach are possible?
- Consider the TOP ranked ideas as inspiration, but don't be limited by them.
- **Focus on NOVELTY.**  Usefulness is secondary at this stage.
- Please return only the ideas, each on a separate line.
- Do not include any explanations or use markdown formatting. Do not add numbering to the ideas.
- The ideas should be around 80-100 words each.
Below you'll find:
- Previously ranked ideas by the team
- New ideas generated in this round by other team members
Your ideas should be radically different from both sets.
```

原檔：`prompts/creative_idea_generation.txt`。來源定位：`generation/prompts.py:396-409`。

### 38. PRACTICAL_IMPROVEMENT

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Your task is to review the following list of creative ideas and refine each one.
- Focus on enhancing their usefulness while carefully preserving the core novelty of the original ideas.
- Please return only the ideas, each on a separate line. 
- Do not include any explanations or use markdown formatting. Do not add numbering to the ideas.
- The ideas should be around 80-100 words each.
```

原檔：`prompts/practical_improvement.txt`。來源定位：`generation/prompts.py:411-417`。

### 39. INTENTION_PROMPT_IDEAS

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Looking at the current list of ideas, please indicate how strongly you feel like responding (1-7)
- Provide your score in the following format: Score:X (replace X with your score).
```

原檔：`prompts/intention_prompt_ideas.txt`。來源定位：`generation/prompts.py:420-423`。

### 40. INTENTION_PROMPT_IDEA

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：生成與討論。原文範圍：完整字串常數。

```text

- Looking at the current idea, please indicate how strongly you feel like responding (1-7)
- Provide your score in the following format: Score:X (replace X with your score).
```

原檔：`prompts/intention_prompt_idea.txt`。來源定位：`generation/prompts.py:425-428`。

### 41. INTENTION_SCORING

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。此定義在作者原始碼中被第 451 行同名定義覆蓋，保存作為公開的早期版本，不是最終運行值。

```text

**Current Idea:**:
{current_idea}


**Suggested Response:**
{agent_potential_response}


**Task:** Considering the task requirement and the current idea, rate the suggested response on its potential contribution. Use a scale of 1 (very low impact) to 10 (very high impact), with one decimal place.
**Scoring Guidelines:**
1: Adds no value (pure agreement, repetition of known information)
2-3: Very low impact (minor clarification, stylistic suggestion)
4-5: Adds some value but could wait (helpful context, alternative perspective)
6-7: Important contribution (significant improvement, corrects misconception)
8-9: Transforms the discussion (crucial missing information, major insight)
10: Discussion cannot proceed without it (fixes dangerous error, provides key breakthrough)
**Instructions:**
- Consider your unique role, expertise, and what others might miss
- Use one decimal place for your score
- Consider both the value and timing of your contribution
- Base your score on your authentic perspective - what YOU bring that others might not
- Avoid clustering around "safe" mid-range scores - be bold in your conviction

Respond first with the numerical score (e.g., '1.0'), followed by a brief explanation of your reasoning on a separate line, starting with "Reason: ".
```

原檔：`prompts/intention_scoring-line-430.txt`。來源定位：`generation/prompts.py:430-449`。

### 42. INTENTION_SCORING

需要提供：相應任務情境；提示要求的先前提案／排名／current_idea／agent_potential_response。

用途：評分。原文範圍：完整字串常數。

```text

**Current Idea:**:
{current_idea}


**Suggested Response:**
{agent_potential_response}


**Task:** Considering the task requirement and the current idea, rate the suggested response on its potential contribution. Use a scale of 1 (very low impact) to 10 (very high impact), with one decimal place.
**Scoring Guidelines:**
1: Adds no value (pure agreement, repetition of known information)
2-3: Very low impact (minor clarification, stylistic suggestion)
4-5: Adds some value but could wait (helpful context, alternative perspective)
6-7: Important contribution (significant improvement, corrects misconception)
8-9: Transforms the discussion (crucial missing information, major insight)
10: Discussion cannot proceed without it (fixes dangerous error, provides key breakthrough)
**Score ONLY based on YOUR perspective:**
- How much does this advance YOUR specific concerns?
- What unique insight do YOU provide about this response?
- Would someone with YOUR background see this differently than others?
- Score based on your perspective, not general helpfulness.

Respond first with the numerical score (e.g., '1.0'), followed by a brief explanation of your reasoning on a separate line, starting with "Reason: ".
```

原檔：`prompts/intention_scoring-line-451.txt`。來源定位：`generation/prompts.py:451-469`。

### 43. Agent personas 與角色組合方式

保留完整角色字典、相同 persona 字串，以及前後綴拼接方式；人口背景是實驗操弄，不是對真實人的推斷。

需要提供：代理編號；三人／六人或相同 persona 條件。

用途：必要上下文。原文範圍：完整公開原檔；原研究沒有發現 persona 能提高整體創意。

```python
import random


BASE_ROLES = {
    "Profile_A": "You are a 22-year-old Black male with an undergraduate degree in computer science. You work as a software engineer in an information technology company. According to the Big Five model, below is your personality profile: Openness to Experience 4.2, Conscientiousness 3.0, Extraversion 3.6, Agreeableness 3.3, and Neuroticism 2.0. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.",
    
    "Profile_B": "You are a 26-year-old Asian female with a graduate degree in public health. You work as a product manager in a healthcare company. According to the Big Five model, below is your personality profile: Openness to Experience 3.2, Conscientiousness 4.0, Extraversion 2.5, Agreeableness 4.5, and Neuroticism 3.2. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.",

    "Profile_C": "You are a 32-year-old White female with a graduate degree in finance. You work as a personal financial advisor in a bank. According to the Big Five model, below is your personality profile: Openness to Experience 3.7, Conscientiousness 3.5, Extraversion 3.0, Agreeableness 3.8, and Neuroticism 2.7. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.",

    "Profile_D": "You are a 25-year-old Chinese female with a graduate degree in art education. You work as an art teacher in a secondary school. According to the Big Five model, below is your personality profile: Openness to Experience 4.5, Conscientiousness 2.8, Extraversion 3.4, Agreeableness 3.9, and Neuroticism 3.5. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.",


    "Profile_E": "You are a 27-year-old White male with an undergraduate degree in chemical engineering. You work as an engineer in an energy company. According to the Big Five model, below is your personality profile: Openness to Experience 3.8, Conscientiousness 3.6, Extraversion 3.1, Agreeableness 3.6, and Neuroticism 2.4. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.",

    "Profile_F": "You are a 28-year-old Asian male with an undergraduate degree in economics. You work as an accountant in an automobile manufacturing company. According to the Big Five model, below is your personality profile: Openness to Experience 3.1, Conscientiousness 4.2, Extraversion 2.6, Agreeableness 4.2, and Neuroticism 2.9. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score."

}

SAME_PERSONA_DESCRIPTION = 'You are a 24-year-old White female with a graduate degree in business and management. You work as a management consultant in a consulting firm. According to the Big Five model, below is your personality profile: Openness to Experience 3.7, Conscientiousness 3.5, Extraversion 3.0, Agreeableness 3.8, and Neuroticism 2.7. These personality scales range from 1 to 5, where 1 indicates a low score and 5 indicates a high score.'
# You can optionally print it to verify
# import json
# print(json.dumps(ALL_PROFILES, indent=4))


def get_randomized_roles_with_fixed_same(number_of_profiles=3):
    """
    Shuffles the base roles (excluding Same_Persona) and assigns them
    to Persona_X keys, prepending an agent identifier.
    Adds the fixed Same_Persona back into the dictionary.
    """
    profiles = list(BASE_ROLES.values())[:number_of_profiles]  # Only first N profiles
    random.shuffle(profiles)

    # Define the keys for the roles being randomized
    keys_to_randomize = [f"Persona_{i+1}" for i in range(number_of_profiles)]

    # Create the dictionary for randomized roles
    randomized_roles = {}
    for i, key in enumerate(keys_to_randomize):
        agent_number = i + 1  # Start agent numbering from 1
        # Optional: Add prefix only to randomized ones, or adjust as needed
        prefix = f"You are Agent {agent_number}. "
        if i < len(profiles):
            randomized_roles[key] = prefix + profiles[i] + " You have the knowledge of this person. You talk like this person. You think like this person."
        else:
            # Handle case where there are fewer profiles than keys
            randomized_roles[key] = prefix + "No profile assigned." # Or just assign empty string, or raise error

    # --- Minimal Change: Add the fixed Same_Persona back ---
    randomized_roles["Same_Persona"] = SAME_PERSONA_DESCRIPTION+ " You have the knowledge of this person. You talk like this person. You think like this person."
    # --- End of Minimal Change ---

    return randomized_roles

# --- Example Usage ---
# This call now generates a ROLES dictionary that includes the fixed
# 'Same_Persona' and randomized 'Persona_1', 'Persona_2', etc.
```

原檔：`upstream/generation/roles.py`。來源定位：`generation/roles.py`。

### 44. Idea harmonization system prompt

搭配同目錄 idea-harmonization-user.txt，把不同來源創意整理成一致語氣後再盲評。

需要提供：原始創意文字（透過 user prompt 提供）。

用途：前處理。原文範圍：完整執行中的 system prompt；不包含已註解掉的舊版。

```text
You are an AI assistant that rephrases ideas. Your main goal is to accurately convey the core meaning of the provided text in a natural, accessible way.

        **Text Processing Instructions:**
        - If the text contains "evolve [X] into [Y]" or similar transformation language, focus only on the final concept (Y) and ignore the initial concept (X).
        - If the text contains multiple ideas with clear section headers (like "---Final Idea---" or "---One Creative Idea---"), focus only on the content under the final/main idea section.
        - If the text contains multiple ideas without clear hierarchy, treat the entire content as one comprehensive idea.
        - Remove any brainstorming artifacts, transitional phrases, or development language that doesn't contribute to the core concept.

        **Writing Style Requirements:**
        - Use a **clear, neutral, and straightforward writing style** regardless of the original text's style.
        - Simplify complex or technical language while preserving core meaning - choose everyday words over specialized terminology when possible.
        - Remove branded terms, metaphorical names in quotes, and elaborate descriptive phrases that don't add essential information.
        - Break down dense technical concepts into simpler, more digestible explanations.
        - Be concise: If the original idea is lengthy, shorten it. If it's already brief, rewrite while preserving its essence and approximate length.
        - Stick to the original meaning: Do not add new information, context, or opinions.
        - Direct output: Provide only the rephrased idea, without introductory or concluding phrases.
        - Use THIRD-PERSON perspective only. Never use "we", "I", "you", "us", or "our" but maintain natural language.
        - Use active voice when possible and replace overly formal or technical language with clear, accessible alternatives.
        - Reduce technical density: If the original lists many technical specifications or components, focus on the main mechanism and primary benefits.
        - Use conversational sentence structure rather than academic or highly technical phrasing.
        
```

原檔：`prompts/idea-harmonization-system.txt`。來源定位：`preprocessing/azure_paraphrase_service.py:98–120`。

### 45. Idea harmonization user prompt

填最大字數與原創意，配合 harmonization system prompt；原研究方法寫約 100 字。

需要提供：{max_words}；{idea}。

用途：前處理。原文範圍：完整 user prompt。

```text
Paraphrase this idea in under {max_words} words using simple, clear language that anyone can understand: {idea}
```

原檔：`prompts/idea-harmonization-user.txt`。來源定位：`preprocessing/azure_paraphrase_service.py:124`。

## 原始程式集合

上方模板另保留完整的來源程式，便於查看常數對應與組裝方式：

- [upstream/generation/prompts.py](upstream/generation/prompts.py)：完整已公開模板；沒有改寫內容。

## 來源與授權

論文授權：arXiv non-exclusive distribution license。模板、程式與資料各自沿用來源授權；逐檔授權、處理方式、固定版本與 SHA-256 列於來源清單。

[arXiv 論文](https://arxiv.org/html/2605.17885v1) · [官方程式固定版本](https://github.com/pitehu/llm_multiagent_creativity/tree/f7e5245a9f6c8a943417ae49b8b3469b6b75424e) · [逐檔來源與授權](../../sources.json)

來源查核與整理日期：2026-11-16。中文導讀為本庫整理；原始模板保留來源文字。
