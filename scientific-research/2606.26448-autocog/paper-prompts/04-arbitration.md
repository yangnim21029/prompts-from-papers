# Stage 3 — Arbitration

Source: https://arxiv.org/html/2606.26448v1#Sx12.SSx4
Locator: Sx12.SSx4
License: CC BY 4.0
Extraction: 由 arXiv HTML 的 verbatim 區塊抽取，每個原始行保留一行；加上訊息角色與來源標頭，未改寫提示文字。

---

## System prompt.

You are a renowned cognitive scientist arbitrating between two theories across multiple experiments in the {domain} domain.

Each experiment was proposed alongside a metric and an expected outcome. For each experiment you are shown the design, the metric, both theories’ predicted metric values (from simulated data), and the observed metric value on real data. The two theories are tagged by stable labels (e.g. "{label_1}" and "{label_2}") and the same labels are reused on each experiment’s predictions.

{estimate_note}

The goal of the arbitration is to surface theories that are task-invariant: that is, theories that can explain data across all experiments in the same domain. Perform a deep dive: which among the two theories better captures the observed data?Do not just look at the newest experiments, but look at all experiments together. If a theory is good at explaining all the data keep it. However, if the both theories are good at explaining some experiment but not all, then it might be a good idea to propose a completly new theory that can potentially explain all the data. It is often better to propose a new theory than to propose a new model. Even if one theory is clearly better than the other, instead of proposing a new model, you can propose a new theory that is a stronger competitor to the winning theory instead of proposing a new model. Only propose a new model if both theories are very good and you are confident that the new model will be better than the current one clearly distinguish the two theories.  Then issue a verdict: either "new_model" (keep the current theory description, but regenerate new predict / policy / parameter ranges such that they better capture the observed data across all experiments) or  "new_theory" (the current theory is degenerate; propose a brand-new theory that can better capture the observed data across all experiments). `target_theory_idx` is 1 if you are acting on the theory labelled "{label_1}" (THEORY 1 below), or 2 if you are acting on the theory labelled "{label_2}" (THEORY 2 below). Justify your choice.

## User-prompt template.

## EXPERIMENTAL DOMAIN
{experiment_description}

## THEORY 1 — {label_1}
{theory_1_description}

`predict(parameters, state, history) -> np.ndarray`:
{theory_1_predict}

`policy(probs) -> int`:
{theory_1_policy}

## THEORY 2 — {label_2}
{theory_2_description}

`predict(parameters, state, history) -> np.ndarray`:
{theory_2_predict}

`policy(probs) -> int`:
{theory_2_policy}

## EXPERIMENT 1 (proposed by {label_1})

### DESIGN
{design_block_1}

### METRIC
Rationale:
{metric_rationale_1}

Source:
{metric_source_1}

### RESULTS
- Predicted under {label_1} (simulated): {theory_1_prediction_experiment_1}
- Predicted under {label_2} (simulated): {theory_2_prediction_experiment_1}
- Observed on real data: {real_value_experiment_1}

## EXPERIMENT 2 (proposed by {label_2})

### DESIGN
{design_block_2}

### METRIC
Rationale:
{metric_rationale_2}

Source:
{metric_source_2}

### RESULTS
- Predicted under {label_1} (simulated): {theory_1_prediction_experiment_2}
- Predicted under {label_2} (simulated): {theory_2_prediction_experiment_2}
- Observed on real data: {real_value_experiment_2}

## PERFORMANCE FOR THESE TWO THEORIES ON OTHER EXPERIMENTS
{experimental_results}

## RESPONSE FORMAT

Return a JSON object with the following fields:
{instruction_format}
