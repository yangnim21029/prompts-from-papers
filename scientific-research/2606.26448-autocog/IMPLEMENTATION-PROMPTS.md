# 官方程式中的完整模板與上下文組裝

本頁屬於 *Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist* 的完整補充材料。保留固定版本原文，與論文實驗版本的關係見[研究與核心模板](README.md)。

SYSTEM_PROMPT 與 TEMPLATE 搭配 render() 組成訊息；保留格式化實驗觀察、估計值、理論程式與歷史回饋的輔助邏輯。

### 1. arbitration — current source

需要提供：design_block_1；design_block_2；domain；estimate_note；experiment_description；experimental_results；i；instruction_format；label_1；label_2；metric_rationale_1；metric_rationale_2；metric_source_1；metric_source_2；obs.metric.metric_source；real_value_experiment_1；real_value_experiment_2；theory_1_description；theory_1_policy；theory_1_predict；theory_1_prediction_experiment_1；theory_1_prediction_experiment_2；theory_2_description；theory_2_policy；theory_2_predict；theory_2_prediction_experiment_1；theory_2_prediction_experiment_2。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

````python
from __future__ import annotations

from typing import TYPE_CHECKING

from src.metric import Estimate, fmt_estimate
from src.prompts.interpret_results import ESTIMATE_NOTE, _fmt  # noqa: F401

if TYPE_CHECKING:
    from src.arbiter_verdict import ArbiterVerdict
    from src.experiment import Experiment
    from src.observation import Round
    from src.observation import Observation

SYSTEM_PROMPT = """\
You are a renowned cognitive scientist arbitrating between two theories across \
multiple experiments in the {domain} domain.

Each experiment was proposed alongside a metric and an expected outcome. For \
each experiment you are shown the design, the metric, both theories' \
predicted metric values (from simulated data), and the observed metric value \
on real data. The two theories are tagged by stable labels (e.g. "{label_1}" \
and "{label_2}") and the same labels are reused on each experiment's \
predictions.

{estimate_note}

The goal of the arbitration is to surface theories that are task-invariant: that is,\
 theories that can explain data across all experiments in the same domain. \
Perform a deep dive: which among the two theories better captures the observed data?\
Do not just look at the newest experiments, but look at all experiments together. \
If a theory is good at explaining all the data keep it. However, if the \
both theories are good at explaining some experiment but not all, then \
it might be a good idea to propose a completly new theory that can potentially \
explain all the data. \
It is often better to propose a new theory than to propose a new model. \
Even if one theory is clearly better than the other, instead of proposing \
a new model, you can propose a new theory that is a stronger competitor to \
the winning theory instead of proposing a new model. \
Only propose a new model if both theories are very good and \
you are confident that the new model will be better than the current one \
clearly distinguish the two theories. \
 Then issue a verdict: either "new_model" (keep the \
current theory description, but regenerate new predict / policy / parameter \
ranges such that they better capture the observed data across all experiments) or \
 "new_theory" (the current theory is degenerate; propose a \
brand-new theory that can better capture the observed data across all experiments). \
`target_theory_idx` is 1 if you are acting on the theory \
labelled "{label_1}" (THEORY 1 below), or 2 if you are acting on the theory \
labelled "{label_2}" (THEORY 2 below). Justify your choice.
"""


TEMPLATE = """\
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
"""


def format_other_experiments(
    others: list["Observation"],
    label_1: str,
    label_2: str,
) -> str:
    """Render a block for each non-current-round observation, showing only
    the two current theories' predictions (by label) alongside the real
    value — no misleading "Candidate (simulated) value" line."""
    if not others:
        return "(no other experiments)"
    blocks: list[str] = []
    for i, obs in enumerate(others, start=3):
        p1 = obs.prediction_by_label(label_1)
        p2 = obs.prediction_by_label(label_2)
        block = (
            f"### Experiment {i}\n"
            f"**Design**\n{obs.experiment.pretty_print_design()}\n\n"
            f"**Metric**\n"
            f"```python\n{obs.metric.metric_source}\n```\n\n"
            f"**Observed (real) value:** {fmt_estimate(obs.real_as_estimate())}\n"
            f"**Predicted under {label_1}:** "
            f"{fmt_estimate(p1.as_estimate() if p1 else None)}\n"
            f"**Predicted under {label_2}:** "
            f"{fmt_estimate(p2.as_estimate() if p2 else None)}"
        )
        blocks.append(block)
    return "\n\n".join(blocks)


def render(
    *,
    experiment_class: type["Experiment"],
    round: "Round",
    arbiter_verdict: type["ArbiterVerdict"],
    other_observations: list["Observation"],
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for arbitrating one round.

    The Round is expected to contain exactly two Observations, one per pi.
    Each Observation carries `proposer_label` (the authoring pi) plus a
    Prediction tagged with the proposer's label (own simulation) and a
    Prediction tagged with the adversary's label (cross-simulation), as
    written by `AutoCog.propose_round`.
    """
    if len(round) != 2:
        raise ValueError(
            f"arbitration.render: expected a round of 2 observations, got {len(round)}."
        )
    obs_1, obs_2 = round[0], round[1]
    label_1 = obs_1.proposer_label or "theory_1"
    label_2 = obs_2.proposer_label or "theory_2"
    theory_1, theory_2 = obs_1.proposer_theory, obs_2.proposer_theory

    def _est(prediction) -> Estimate | None:
        # In each obs, the proposer's prediction is tagged with its own label;
        # the cross prediction with the other pi's label. Wrap as Estimate so
        # downstream rendering picks up both value AND variance.
        return prediction.as_estimate() if prediction is not None else None

    t1_pred_e1 = _est(obs_1.prediction_by_label(label_1))
    t2_pred_e1 = _est(obs_1.prediction_by_label(label_2))
    t1_pred_e2 = _est(obs_2.prediction_by_label(label_1))
    t2_pred_e2 = _est(obs_2.prediction_by_label(label_2))

    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name,
        label_1=label_1,
        label_2=label_2,
        estimate_note=ESTIMATE_NOTE,
    )
    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        label_1=label_1,
        label_2=label_2,
        # THEORY 1
        theory_1_description=theory_1.description,
        theory_1_predict=theory_1.predict_source,
        theory_1_policy=theory_1.policy_source,
        # THEORY 2
        theory_2_description=theory_2.description,
        theory_2_predict=theory_2.predict_source,
        theory_2_policy=theory_2.policy_source,
        # EXPERIMENT 1 — design rationale is already inside pretty_print()
        design_block_1=obs_1.experiment.pretty_print(),
        metric_rationale_1=obs_1.metric.rationale or "(no rationale provided)",
        metric_source_1=obs_1.metric.metric_source,
        theory_1_prediction_experiment_1=fmt_estimate(t1_pred_e1),
        theory_2_prediction_experiment_1=fmt_estimate(t2_pred_e1),
        real_value_experiment_1=fmt_estimate(obs_1.real_as_estimate()),
        # EXPERIMENT 2 — design rationale is already inside pretty_print()
        design_block_2=obs_2.experiment.pretty_print(),
        metric_rationale_2=obs_2.metric.rationale or "(no rationale provided)",
        metric_source_2=obs_2.metric.metric_source,
        theory_1_prediction_experiment_2=fmt_estimate(t1_pred_e2),
        theory_2_prediction_experiment_2=fmt_estimate(t2_pred_e2),
        real_value_experiment_2=fmt_estimate(obs_2.real_as_estimate()),
        # OTHER EXPERIMENTS
        experimental_results=format_other_experiments(
            other_observations, label_1, label_2
        ),
        # FORMAT
        instruction_format=arbiter_verdict.instruction_format(),
    )
    return system_prompt, user_prompt
````

原檔：`upstream/src/prompts/arbitration.py`。來源定位：`src/prompts/arbitration.py`。

### 2. experiment_proposal — current source

需要提供：advocating_description；competing_description；design_header；domain；experiment_description；i；instruction_format；introduction_text；ledger。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.experiment import Experiment
    from src.theory import Theory


SYSTEM_PROMPT = """\
You are a renowned cognitive scientist designing an experiment in the {domain} domain.

Your goal is to be an adversarial collaborator: propose a design whose outcomes would be predicted by \
your advocated theory but NOT by the competing theory. Both are provided below.

A useful proposal targets a *quantitative* dissociation between the two theories — \
how they respond differently to specific stimuli in addition to differences in overall \
performance.
"""


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}

{design_header}

Subjects see the following instructions:
{introduction_text}

## ADVOCATED THEORY
{advocating_description}

## COMPETING THEORY
{competing_description}

## ALREADY-EXPLORED EXPERIMENTS (do not repeat)
{ledger}

## RESPONSE FORMAT
Return a JSON object with the following fields:
{instruction_format}
"""





def _format_ledger(experiments: list["Experiment"]) -> str:
    if not experiments:
        return "(none yet)"
    return "\n\n".join(
        f"[{i}] {e.rationale or '(no rationale)'}" for i, e in enumerate(experiments)
    )


def render(
    *,
    experiment_class: type["Experiment"],
    advocating: "Theory",
    competing: "Theory",
    ledger: list["Experiment"] | None = None,
) -> tuple[str, str]:
    """
    Returns (system_prompt, user_prompt) for proposing an experiment.

    All design facts (domain description, n_blocks/n_repeats, instructions, JSON
    schema, parameter variables) are pulled directly from `experiment_class` —
    one source of truth.
    """
    system_prompt = SYSTEM_PROMPT.format(domain=experiment_class.name)

    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        design_header=experiment_class.pretty_print_header(),
        introduction_text=experiment_class.introduction_text,
        advocating_description=advocating.pretty_print(),
        competing_description=competing.pretty_print(),
        ledger=_format_ledger(ledger or []),
        instruction_format=experiment_class.instruction_format(),
    )
    return system_prompt, user_prompt
```

原檔：`upstream/src/prompts/experiment_proposal.py`。來源定位：`src/prompts/experiment_proposal.py`。

### 3. feedback — current source

需要提供：arbiter_block；arbiter_target_idx；best_k；cur_marker；delta；delta_now；domain；estimate_note；experiment_description；experimental_results；header；i；instruction_format；it.rationale；k；last_index；loss_trajectory_block；marker；next_label；obs.metric.metric_source；outcome_line；p.label；prior_critiques_block；rendered；target_label；theory_description；theory_parameters；theory_policy；theory_predict；theory_rationale；v；value_block。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

````python
"""Prompt: critique a freshly proposed candidate theory/model.

Used by the `Feedback` agent inside `Improver` / `TheoryGenerator`'s inner
loop. The candidate is simulated on every existing experiment (each
`Observation` in the pool); for each one we have a real_value (collected on
human/ground-truth data) and a candidate_value (the candidate's metric on
its own simulated data). The feedback agent reads those side-by-side and
returns a `FeedbackVerdict` (`"continue"` or `"regenerate"`).
"""

from __future__ import annotations

from typing import TYPE_CHECKING
   
from src.metric import Estimate, fmt_estimate
from src.prompts.interpret_results import ESTIMATE_NOTE, _fmt

if TYPE_CHECKING:
    from src.arbiter_verdict import FeedbackVerdict
    from src.experiment import Experiment
    from src.feedback import PriorIteration
    from src.observation import Observation
    from src.theory import Theory


SYSTEM_PROMPT = """\
You are a renowned cognitive scientist critiquing a freshly proposed candidate \
theory and model in the {domain} domain.

The candidate has been simulated on every previously run experiment. For each \
experiment you are shown the design, the metric, the value the metric takes \
on real data, and the value it takes on the \
candidate's simulated data.

{estimate_note}

The goal of the feedback is to SURFACE theories that are EXPERIMENT-INVARIANT: that is,\
theories that explain data across multiple experiments. \

Your task is to determine whether the candidate captures the human/real behavior well enough \
across these experiments. Return a verdict:
  * "continue"   — the candidate is good enough; carry on.
  * "regenerate" — the candidate fails to capture the empirical pattern; \
the proposing agent must produce a new candidate, taking your rationale \
into account.

Justify the verdict with a concrete diagnosis (which experiments fail, in \
what direction, what mechanism is likely missing or miscalibrated).

## SCOPE OF YOUR CRITIQUE — STAY INSIDE THE ARBITER'S MECHANISM FAMILY
When an "## ARBITER RECOMMENDATION" block is present below, the proposer was \
explicitly instructed to implement the mechanism family the arbiter prescribed. \
Your job is to grade FIT QUALITY *within that prescribed family*, not to relitigate \
which family should be used — that is the arbiter's call, made one level above \
this loop.

Concretely:
  * If the candidate misses the data, you may push for MINOR ADJUSTMENTS that \
keep the prescribed mechanism intact: tightening / widening parameter ranges, \
adding a temperature, swapping a normalization scheme, fixing a softmax / \
distance metric, re-balancing attention weights, fixing a learning-rate sign, \
correcting a bug in the gating or recurrence, etc.
  * You MUST NOT recommend switching to a different mechanism family. Such a \
switch is the arbiter's prerogative; recommending it here will mislead the \
proposer into oscillating between families across iterations.
  * Also grade FAITHFULNESS to the recommendation explicitly: if the candidate \
has clearly drifted into a different family than the one prescribed, say so in \
the rationale and ask for a return to the prescribed family — again, with \
minor adjustments, not a re-design.

## ACCEPT GATE — HOW THE LOOP DECIDES WHAT TO BUILD ON NEXT
This propose-loop has a programmatic accept gate. After every iteration the \
candidate's `aggregate_loss` is compared against the running-best loss \
(`accepted_loss`):
  * `loss < accepted_loss` → ACCEPTED. The candidate becomes the new \
running-best base; the next iteration's proposer will build on THIS candidate.
  * `loss >= accepted_loss` → REJECTED. The base is unchanged; the next \
iteration's proposer will build on the SAME `accepted` candidate again, with \
your new feedback on top. Rejected candidates are discarded — the loop guarantees \
the base never regresses, so you do NOT need to ask the proposer to "revert" \
anything; that already happens for free.

Two consequences for your verdict:
  * If the candidate you are grading was REJECTED by the gate, returning \
`"continue"` is silently downgraded to `"regenerate"` (returning a worse \
candidate would defeat the gate). Spend your rationale on a NEW direction the \
proposer should try on top of the unchanged accepted base, not on defending the \
rejected attempt.
  * If the candidate was ACCEPTED, you can return `"continue"` to stop the loop \
and ship this candidate, or `"regenerate"` to keep tuning further.

## LEARN FROM YOUR OWN PAST ADVICE
When a "## YOUR PRIOR CRITIQUES" block is present below, each prior iteration \
ends with an "Outcome of your advice" line that says whether the next candidate \
the proposer produced was ACCEPTED (your advice helped — its loss strictly \
beat the running best) or REJECTED (your advice didn't help — the proposer \
discarded the result and reset to the previous accepted base). This is the \
loop's ground-truth signal on whether *your own previous critique was good*. \
Use it explicitly:
  * If a previous piece of advice was ACCEPTED, it is OK to repeat / extend it. \
Reinforce in the same direction.
  * If a previous piece of advice was REJECTED, do NOT repeat the same \
recommendation; in your new rationale, briefly acknowledge that the previous \
push in that direction was rejected by the gate and try a different in-family \
knob (or a smaller step in the same direction) instead.
  * If you find yourself oscillating (e.g. iter 1 said "increase α", iter 2 \
said "decrease α", iter 3 about to say "increase α" again), STOP and recommend \
a value between the two flanking iterations instead.
  * The "## LOSS TRAJECTORY" block at the top of the user prompt summarises the \
same information at the loop level — consult it before issuing a new \
regenerate-with-direction recommendation.
"""
# If a "Candidate trajectory (this loop)" block is shown for an experiment, \
# inspect it: a candidate that overshot in the previous iteration and now \
# undershoots (or vice-versa) is oscillating. In that case do NOT recommend \
# "swap direction" again; instead recommend bisection — a smaller step, a \
# parameter value between the two flanking iterations, or a mechanism that \
# trades off the two extremes — so the next candidate lands between the \
# prior two on this metric.


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}
{arbiter_block}
## CANDIDATE THEORY
{theory_description}

`predict(parameters, state, history) -> np.ndarray`:
{theory_predict}

`policy(probs) -> int`:
{theory_policy}

`parameters`:
{theory_parameters}

`rationale`:
{theory_rationale}
{loss_trajectory_block}
## EXPERIMENTAL RESULTS (candidate vs real, per experiment)
{experimental_results}
{prior_critiques_block}
## RESPONSE FORMAT

Return a JSON object with the following fields:
{instruction_format}
"""


def _format_parameters(parameters: dict[str, str]) -> str:
    if not parameters:
        return "(none)"
    return "\n".join(f"- {k}: {v}" for k, v in parameters.items())


def _format_other_predictions(obs: "Observation") -> str:
    """Render previously-recorded theory predictions on this Observation's
    metric, one per line, as a calibration reference for the critic.
    Each entry shows both the point estimate and the between-subject
    variance (the same `value (var=...)` shape as everywhere else)."""
    if not obs.predicted_values:
        return "(none)"
    lines = [
        f"- {p.label}: {fmt_estimate(p.as_estimate())}"
        for p in obs.predicted_values
    ]
    return "\n".join(lines)


def _fmt_loss(loss: float | None) -> str:
    """Render an aggregate loss value compactly. `None` is shown as `n/a`,
    `+inf` as `+inf` (unscorable), everything else with 4 decimals."""
    if loss is None:
        return "n/a"
    if loss == float("inf"):
        return "+inf"
    if loss == float("-inf"):
        return "-inf"
    return f"{loss:.4f}"


def _accept_marker(accepted: bool | None) -> str:
    """Render the accept-gate verdict for an iteration. `True` → ACCEPTED
    (became the new running-best base), `False` → REJECTED (discarded;
    base unchanged), `None` → unknown (used for the iter-0 row when no
    accept decision has been recorded yet)."""
    if accepted is None:
        return "?"
    return "ACCEPTED" if accepted else "REJECTED"


def _format_trajectory(
    obs_idx: int,
    real_value: float | None,
    current: "Estimate",
    prior_iterations: list["PriorIteration"] | None,
) -> str:
    """Render a per-experiment "candidate over iterations" trajectory.

    `obs_idx` is the position of this observation inside the loop's
    `candidate_results` list. We pull the `Estimate` at `obs_idx` from each
    prior iteration's estimate list (same indexing as the current `results`).

    The trajectory makes oscillation visible. The Δ-vs-real number compares
    point estimates only (variance is shown alongside but not subtracted).
    Example:
        iter 1: 0.6704 (var=0.0210)  (Δ vs real -0.1550)
        iter 2: 0.9858 (var=0.0040)  (Δ vs real +0.1610)
        iter 3 (current): 0.6371 (var=0.0160)  (Δ vs real -0.1880)
    so the critic can recommend bisection / smaller steps instead of
    flipping direction every iteration.
    """
    rows: list[str] = []
    if prior_iterations:
        for k, it in enumerate(prior_iterations, start=1):
            est = it.estimates[obs_idx] if obs_idx < len(it.estimates) else None
            delta = (
                f" (Δ vs real {est.value - real_value:+.4f})"
                if est is not None
                and est.value is not None
                and real_value is not None
                else ""
            )
            rows.append(f"  - iter {k}: {fmt_estimate(est)}{delta}")
    delta_now = (
        f" (Δ vs real {current.value - real_value:+.4f})"
        if current.value is not None and real_value is not None
        else ""
    )
    rows.append(
        f"  - iter {len(prior_iterations or []) + 1} (current): "
        f"{fmt_estimate(current)}{delta_now}"
    )
    return "**Candidate trajectory (this loop):**\n" + "\n".join(rows)


def format_candidate_results(
    results: list[tuple["Observation", "Estimate"]],
    *,
    prior_iterations: list["PriorIteration"] | None = None,
) -> str:
    """Render `(observation, candidate_estimate)` pairs as the results block.

    Each entry shows the experimental design, the metric, the observed
    real value (with variance), the candidate's simulated value (with
    variance), and (when `prior_iterations` is non-empty) the per-iteration
    trajectory of candidate estimates for the same observation in this
    propose-loop, plus the estimates produced by every other theory
    previously evaluated against this metric.
    """
    if not results:
        return "(no observations to score against)"
    blocks: list[str] = []
    for i, (obs, est) in enumerate(results, start=1):
        if prior_iterations:
            value_block = _format_trajectory(
                i - 1, obs.real_value, est, prior_iterations
            )
        else:
            value_block = (
                f"**Candidate (simulated) value:** {fmt_estimate(est)}"
            )
        block = (
            f"### Experiment {i}\n"
            f"**Design**\n{obs.experiment.pretty_print_design()}\n\n"
            f"**Metric**\n"
            f"```python\n{obs.metric.metric_source}\n```\n\n"
            f"**Observed (real) value:** {fmt_estimate(obs.real_as_estimate())}\n"
            f"{value_block}\n"
            f"**Other theories' values on this metric (for reference):**\n"
            f"{_format_other_predictions(obs)}"
        )
        blocks.append(block)
    return "\n\n".join(blocks)


def _format_loss_trajectory_block(
    prior_iterations: list["PriorIteration"] | None,
    current_loss: float | None,
    current_accepted: bool | None,
    accepted_loss: float | None,
) -> str:
    """Render the propose-loop's `aggregate_loss` trajectory with the
    accept-gate decision per iteration.

    Each row carries the iteration's `aggregate_loss` plus an
    ACCEPTED/REJECTED tag from the loop's accept gate (programmatic,
    `loss < accepted_loss`). The current candidate's accept status is
    derived from `current_accepted` directly; prior iterations carry it
    on their `PriorIteration.accepted` field.

    Returns "" when there is nothing to render (no prior iterations AND
    no current loss) so iter-0 calls without state stay unchanged.
    """
    if not prior_iterations and current_loss is None:
        return ""
    rows: list[str] = []
    accepted_iters: list[tuple[int, float]] = []
    last_index = len(prior_iterations or []) + 1  # current row's 1-based index
    for k, it in enumerate(prior_iterations or [], start=1):
        rows.append(
            f"- iter {k}: loss={_fmt_loss(it.loss)} "
            f"-> {_accept_marker(it.accepted)}"
        )
        if it.accepted and it.loss != float("inf"):
            accepted_iters.append((k, it.loss))
    # Current candidate row.
    cur_marker = _accept_marker(current_accepted)
    rows.append(
        f"- iter {last_index} (current candidate you are grading): "
        f"loss={_fmt_loss(current_loss)} -> {cur_marker}"
    )
    if current_accepted and current_loss is not None and current_loss != float("inf"):
        accepted_iters.append((last_index, current_loss))
    # Running-best summary line.
    if accepted_iters:
        best_k, best_l = min(accepted_iters, key=lambda kl: kl[1])
        running_best_line = (
            f"\nRunning-best (last accepted) base: iter {best_k} at loss="
            f"{_fmt_loss(best_l)}."
        )
    elif accepted_loss is not None and accepted_loss != float("inf"):
        running_best_line = (
            f"\nRunning-best (last accepted) base: loss={_fmt_loss(accepted_loss)}."
        )
    else:
        running_best_line = (
            "\nNo accepted base yet (this is iter 1; any finite loss will be "
            "auto-accepted)."
        )
    return (
        "\n## LOSS TRAJECTORY (this propose-loop)\n"
        "Aggregate loss across iterations of THIS propose-loop "
        "(lower = better, 0 = perfect, `+inf` = unscorable). The "
        "ACCEPTED / REJECTED tag is the loop's programmatic accept-gate "
        "decision: `loss < accepted_loss` -> ACCEPTED (becomes new base), "
        "else REJECTED (base unchanged). Use this together with the "
        "per-experiment values below to grade fit-quality AND your own "
        "past advice (see `## YOUR PRIOR CRITIQUES` below).\n\n"
        + "\n".join(rows)
        + running_best_line
        + "\n"
    )


def _format_prior_critiques(
    prior_iterations: list["PriorIteration"] | None,
    current_loss: float | None,
    current_accepted: bool | None,
) -> str:
    """Render the critic's own past verdicts + rationales, each annotated
    with whether the candidate the proposer produced AFTER following that
    advice was ACCEPTED (advice helped — strict loss improvement) or
    REJECTED (advice didn't help — candidate discarded by the gate) by
    the propose-loop's accept gate.

    The "Outcome of your advice" line is the headline learning signal:
    advice in iter k caused the candidate in iter k+1, whose acceptance
    status is on `prior_iterations[k]` (or, for the most recent prior
    critique, on `current_accepted`).

    Per-experiment values for those iterations are shown inline in
    `format_candidate_results` so the reader can read the full picture
    next to the experiment, not as a separate disconnected section.
    """
    if not prior_iterations:
        return ""
    blocks: list[str] = []
    for i, it in enumerate(prior_iterations, start=1):
        is_last = i == len(prior_iterations)
        if is_last:
            next_loss = current_loss
            next_accepted = current_accepted
            next_label = "CURRENT candidate"
        else:
            next_loss = prior_iterations[i].loss
            next_accepted = prior_iterations[i].accepted
            next_label = f"iter {i + 1} candidate"
        marker = _accept_marker(next_accepted)
        outcome_line = (
            f"**Outcome of your advice:** iter {i} candidate loss="
            f"{_fmt_loss(it.loss)} -> {next_label} loss="
            f"{_fmt_loss(next_loss)} -> the gate marked it {marker}."
        )
        header = (
            f"### Iteration {i} (most recent)" if is_last else f"### Iteration {i}"
        )
        blocks.append(f"{header}\n{it.rationale}\n\n{outcome_line}")
    rendered = "\n\n".join(blocks)
    return (
        "\n## YOUR PRIOR CRITIQUES (for this propose-loop)\n"
        "Each block is one of YOUR previous critique iterations: the verdict "
        "you returned, the interpretation and rationale you wrote, and an "
        "**Outcome of your advice** line that says whether the candidate the "
        "proposer produced AFTER following your advice was ACCEPTED (your "
        "advice helped — its loss strictly beat the running-best) or REJECTED "
        "(your advice didn't help — the gate discarded the candidate). Use "
        "this self-history to (a) reinforce advice that was ACCEPTED, "
        "(b) avoid repeating advice that was REJECTED, and (c) detect your "
        f"own oscillation across iterations.\n\n{rendered}\n"
    )


def _format_arbiter_block(
    arbiter_guide: str | None,
    arbiter_theory_labels: tuple[str | None, str | None] | None,
    arbiter_target_idx: int | None,
) -> str:
    """Render the arbiter's recommendation as a top-level critic-facing block.

    The arbiter's free-text recommendation refers back to its own
    `THEORY 1` / `THEORY 2` headings (anchored to `pi_N` labels in the
    arbitration prompt). Once that recommendation is forwarded into the
    feedback critic, that anchoring is gone, so we re-emit a small key
    above the guide text. Returns "" when no guide is supplied — legacy
    callers stay unchanged.

    The block is the critic's anchor for "stay inside this mechanism
    family" — it pairs with the SCOPE clause in the system prompt.
    """
    if not arbiter_guide:
        return ""
    lines: list[str] = ["", "## ARBITER RECOMMENDATION (mechanism family the proposer was told to implement)"]
    if (
        arbiter_theory_labels
        and arbiter_theory_labels[0] is not None
        and arbiter_theory_labels[1] is not None
    ):
        lines.append(
            "The arbiter labelled this round's two theories in its recommendation as follows:"
        )
        lines.append(f"- THEORY 1 = `{arbiter_theory_labels[0]}`")
        lines.append(f"- THEORY 2 = `{arbiter_theory_labels[1]}`")
        if arbiter_target_idx in (1, 2):
            target_label = arbiter_theory_labels[arbiter_target_idx - 1]
            lines.append(
                f"- The recommendation below acts on THEORY {arbiter_target_idx} "
                f"(= `{target_label}`)."
            )
        lines.append("")
    lines.append(arbiter_guide.rstrip())
    lines.append("")
    return "\n".join(lines) + "\n"


def render(
    *,
    experiment_class: type["Experiment"],
    theory: "Theory",
    candidate_results: list[tuple["Observation", "Estimate"]],
    feedback_verdict: type["FeedbackVerdict"],
    prior_iterations: list["PriorIteration"] | None = None,
    current_loss: float | None = None,
    current_accepted: bool | None = None,
    accepted_loss: float | None = None,
    arbiter_guide: str | None = None,
    arbiter_theory_labels: tuple[str | None, str | None] | None = None,
    arbiter_target_idx: int | None = None,
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for critiquing one candidate.

    `candidate_results` is `[(Observation, Estimate(value, variance)), ...]`;
    one entry per existing experiment the candidate was simulated on.

    `prior_iterations` is the chronological history of this propose-loop as
    `PriorIteration(rationale, estimates, loss, accepted)` entries. The
    estimate list for each iteration is in the SAME order as
    `candidate_results`; `loss` is that iteration's `aggregate_loss`;
    `accepted` is the loop's programmatic accept-gate decision. The
    prompt uses this to render (a) a per-experiment trajectory of
    candidate estimates so the critic can detect oscillation and
    recommend bisection, and (b) a `## YOUR PRIOR CRITIQUES` block where
    each prior iteration's rationale is annotated with whether the next
    candidate was ACCEPTED (advice helped) or REJECTED (advice didn't
    help) — turning the loop into a closed-loop signal the critic can
    learn from.

    `current_loss` is `aggregate_loss` of the candidate being critiqued
    in THIS call. `current_accepted` is whether the loop's accept gate
    will keep that candidate as the new running-best base (True) or
    discard it (False). `accepted_loss` is the running-best loss the
    candidate had to beat. Together they drive the `## LOSS TRAJECTORY`
    block and the "Outcome of your advice" line on the most-recent
    prior critique.

    `arbiter_guide` (+ optional `arbiter_theory_labels` /
    `arbiter_target_idx`) is the recommendation that drove this propose
    loop in the first place. When supplied, it's rendered verbatim under
    a top-level ARBITER RECOMMENDATION block so the critic knows which
    mechanism family the proposer was told to implement and can grade
    fit-quality WITHIN that family rather than recommending a switch
    (mechanism-family switches are the arbiter's prerogative; this loop
    only tunes within the prescribed family).
    """
    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name, estimate_note=ESTIMATE_NOTE
    )
    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        arbiter_block=_format_arbiter_block(
            arbiter_guide, arbiter_theory_labels, arbiter_target_idx
        ),
        theory_description=theory.description,
        theory_predict=theory.predict_source,
        theory_policy=theory.policy_source,
        theory_parameters=_format_parameters(theory.parameters),
        theory_rationale=theory.rationale or "(none)",
        loss_trajectory_block=_format_loss_trajectory_block(
            prior_iterations, current_loss, current_accepted, accepted_loss
        ),
        experimental_results=format_candidate_results(
            candidate_results, prior_iterations=prior_iterations
        ),
        prior_critiques_block=_format_prior_critiques(
            prior_iterations, current_loss, current_accepted
        ),
        instruction_format=feedback_verdict.instruction_format(),
    )
    return system_prompt, user_prompt
````

原檔：`upstream/src/prompts/feedback.py`。來源定位：`src/prompts/feedback.py`。

### 4. interpret_results — current source

需要提供：advocating_description；advocating_policy；advocating_predict；competing_description；competing_policy；competing_predict；design_header；domain；estimate_note；experiment_block；experiment_description；metric_rationale；metric_source；predicted_adversary；predicted_self；real_value。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

```python
from __future__ import annotations

from typing import TYPE_CHECKING

from src.metric import Estimate, fmt_estimate

if TYPE_CHECKING:
    from src.experiment import Experiment
    from src.metric import Metric
    from src.theory import Theory


# Single source of truth for the "what do these two numbers mean?" note.
# Imported by every prompt that displays metric values so the explanation
# is consistent across the system.
ESTIMATE_NOTE = (
    "Each metric value below is shown as `point_estimate (var=X)`, where "
    "`point_estimate` is `metric(data)` evaluated on the full pooled "
    "dataset and `var` is the population (between-subject) variance of "
    "the same metric re-applied per `subject_id`. The point estimate is "
    "the canonical scalar; `var` reports how consistent that estimate is "
    "across subjects (lower = more consistent). `var=n/a` means the "
    "metric could not be applied to a single-subject slice."
)


SYSTEM_PROMPT = """\
You are a renowned cognitive scientist interpreting the results of an experiment you \
designed in the {domain} domain.

You pre-registered a metric expected to be HIGHER under your advocated theory \
than under the competing theory. Below you are shown both theories, the \
experimental design, the metric, the metric's predicted value under each \
theory (from simulated data), and its observed value on the real data.

{estimate_note}

Write a freeform interpretation: does the observed value support the \
advocated theory, the competing theory, neither, or both? Flag any \
confounds, alternative explanations, or weaknesses in the design or metric \
that should temper the conclusion. Be honest about ambiguity — do not \
overclaim.
"""


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}

{design_header}

## CHOSEN EXPERIMENTAL DESIGN
{experiment_block}

## ADVOCATED THEORY
{advocating_description}

`predict(parameters, state, history) -> np.ndarray`:
{advocating_predict}

`policy(probs) -> int`:
{advocating_policy}

## COMPETING THEORY
{competing_description}

`predict(parameters, state, history) -> np.ndarray`:
{competing_predict}

`policy(probs) -> int`:
{competing_policy}

## METRIC
Rationale:
{metric_rationale}

Source:
{metric_source}

## RESULTS
- Predicted under advocated theory (simulated): {predicted_self}
- Predicted under competing theory (simulated): {predicted_adversary}
- Observed on real data: {real_value}

## INTERPRETATION
Write your interpretation below as plain prose. Cover, at minimum:
1. Whether the observed value is closer to the advocated or competing prediction.
2. Whether the qualitative pattern targeted by the design appears in the data.
3. Confounds, alternative explanations, or weaknesses to flag.
4. What experiment or metric should come next, and why.
"""


def _fmt(value: float | None) -> str:
    """Render a bare scalar (no variance attached). Kept for callers that
    still pass plain floats (e.g. trajectory tables that only carry the
    point estimate). For `Estimate`-shaped values use `fmt_estimate`."""
    return "n/a" if value is None else f"{value:.4f}"


def render(
    *,
    experiment_class: type["Experiment"],
    experiment: "Experiment",
    metric: "Metric",
    advocating: "Theory",
    competing: "Theory",
    predicted_self: "Estimate | None",
    predicted_adversary: "Estimate | None",
    real: "Estimate | None",
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for interpreting a round's results.

    `predicted_self`, `predicted_adversary`, `real` are `Estimate` namedtuples
    (`(value, variance)`) — point estimate plus between-subject variance.
    Both numbers get rendered in the user prompt; the system prompt
    explains what they mean.

    The response is freeform text — no JSON schema is enforced — because the
    interpretation is consumed by a human (or another LLM step) rather than
    executed as code.
    """
    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name, estimate_note=ESTIMATE_NOTE
    )

    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        design_header=experiment_class.pretty_print_header(),
        experiment_block=experiment.pretty_print(),
        advocating_description=advocating.description,
        advocating_predict=advocating.predict_source,
        advocating_policy=advocating.policy_source,
        competing_description=competing.description,
        competing_predict=competing.predict_source,
        competing_policy=competing.policy_source,
        metric_rationale=metric.rationale or "(no rationale provided)",
        metric_source=metric.metric_source,
        predicted_self=fmt_estimate(predicted_self),
        predicted_adversary=fmt_estimate(predicted_adversary),
        real_value=fmt_estimate(real),
    )
    return system_prompt, user_prompt
```

原檔：`upstream/src/prompts/interpret_results.py`。來源定位：`src/prompts/interpret_results.py`。

### 5. metric_proposal — current source

需要提供：advocating_description；competing_description；design_header；domain；experiment_block；experiment_description；i；instruction_format；k；ledger；m.metric_source；outcome；output_columns；real_n_subjects；v。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.experiment import Experiment
    from src.metric import Metric
    from src.theory import Theory


SYSTEM_PROMPT = """\
You are a psychology researcher proposing a metric in the {domain} domain.

Your goal is adversarial: propose a metric that DISCRIMINATES the two theories — \
i.e., its value, computed on data simulated under your advocated theory, should be \
as far as possible from its value computed on data simulated under the competing \
theory. The direction of the gap does not matter; what matters is that the two \
theories produce visibly different numbers on this metric. The metric is computed \
on the data collected from the experimental design provided in the prompt. Produce \
a metric where you're prediction will be much more accurate than the competing \
theory's prediction on human data.

Your metric is a Python function

    metric(data: pd.DataFrame) -> float

Available imports inside `metric`:
- numpy as np
- pandas as pd

The system evaluates your metric in two ways and reports the pair as \
`point_estimate (var=between_subject_variance)` everywhere downstream:
- `point_estimate` is `metric(data)` applied to the FULL pooled DataFrame \
(all subjects together) — the canonical scalar;
- `between_subject_variance` is the population variance (`ddof=0`) of \
`metric(subj_df)` re-applied per `subject_id`, summarising how stable the \
metric is across subjects. If your metric only makes sense on multi-subject \
data this will fall back to `n/a` and the metric is rejected (the \
acceptance test below cannot run without it). Prefer metrics that work \
both on the pooled DataFrame and on a single subject's slice.

Acceptance rule: the system simulates each theory and runs Welch's \
two-sample t-test on `(point_estimate_self, between_subject_variance_self, N)` \
vs. `(point_estimate_adv, between_subject_variance_adv, N)`, where N is the \
number of HUMAN subjects the experiment will actually be run with (a fixed \
small number, currently {real_n_subjects}). Your metric is admitted iff the \
two-sided p-value is below the significance level (currently \
alpha={alpha:g}). Implication: a large between-theory gap is NOT enough — if \
either theory's metric is also highly variable across subjects, N humans \
won't reliably distinguish them and the metric will be rejected. Aim for \
contrasts that are both large in mean AND tight per subject.

Do NOT propose metrics that are trivially true for your theory.
"""


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}

{design_header}

## CHOSEN EXPERIMENTAL DESIGN
{experiment_block}

## ADVOCATED THEORY
{advocating_description}

## COMPETING THEORY
{competing_description}

## DATA SCHEMA
Your metric receives a tidy per-trial pandas DataFrame stacking all subjects \
(rows grouped by `subject_id`, in trial order). Columns:
{output_columns}

## IMPLEMENTATION GUARDRAILS
Any column in the schema above whose description names a list / tuple / \
np.ndarray (i.e. a per-trial sequence of values) holds non-scalar cells. \
Those cells are NOT hashable, so operations that hash row values fail with \
`TypeError: unhashable type: 'list'`. Treating `<seq_col>` as a placeholder \
for any such sequence-valued column:
- Avoid: `data.groupby('<seq_col>')`, `data['<seq_col>'].value_counts()`, \
    `data['<seq_col>'].nunique()`, `data['<seq_col>'].unique()` (returns \
    an object array but downstream `set()` / `in dict` will crash), \
    `set(data['<seq_col>'])`, `data['<seq_col>'].isin([...])` against list \
    values, or using a list cell as a dict key.
- If you need a hashable surrogate, project to one first, e.g.:
    - `data['<seq_col>_key'] = data['<seq_col>'].apply(tuple)` then group by `<seq_col>_key`
    - `data['<seq_col>_str'] = data['<seq_col>'].apply(lambda x: ''.join(map(str, x)))`
    Scalar columns (ints, floats, strings like `subject_id`, integer \
    responses, etc.) hash fine and can be used directly.
- Generator expressions inside function calls like `map()` or `join()` MUST be \
    parenthesized. For example:
    - WRONG: `map(str, int(v) for v in x)` → SyntaxError
    - RIGHT: `map(str, (int(v) for v in x))` or use a list comp: `[str(int(v)) for v in x]`
- Always verify your code is syntactically valid Python before returning it.

## METRICS YOU ALREADY TRIED AND FAILED ON
Each entry below is a metric you previously proposed in this round that did \
NOT discriminate the two theories at the human sample size — either it \
errored, its between-subject variance was unavailable, or Welch's t-test on \
`(self mean, self var, N)` vs. `(adv mean, adv var, N)` returned p ≥ alpha. \
The `outcome` line is the simulation result (means, between-subject \
variances, t-statistic and p-value at the human N) on the same `data_self` \
/ `data_adv` your next metric will be evaluated on. Use the numbers to see \
where your hypothesised contrast collapsed — small mean gap, large \
per-subject variance, or both — and propose something qualitatively \
different. Don't repeat the same idea with cosmetic tweaks.
{ledger}

## RESPONSE FORMAT
Return a JSON object with the following fields:
{instruction_format}
"""


def _format_columns(columns: dict[str, str]) -> str:
    if not columns:
        return "(none)"
    return "\n".join(f"- {k}: {v}" for k, v in columns.items())


def _format_ledger(failed: list[tuple["Metric", str]]) -> str:
    """Render past failed metric attempts with their numeric outcomes.

    Each item is `(metric, outcome)`, where `outcome` is the human-readable
    result line printed by the orchestrator for that attempt — e.g.
    `self_sim=0.9600 adversary_sim=2.2675 -> reject` or
    `evaluation failed (TypeError: unhashable type: 'list')`.
    """
    if not failed:
        return "(none yet)"
    return "\n\n".join(
        f"[{i}] rationale: {m.rationale or '(no rationale)'}\n"
        f"metric_source:\n{m.metric_source}\n"
        f"outcome: {outcome}"
        for i, (m, outcome) in enumerate(failed)
    )


def render(
    *,
    experiment_class: type["Experiment"],
    experiment: "Experiment",
    advocating: "Theory",
    competing: "Theory",
    metric_class: type["Metric"],
    ledger: list[tuple["Metric", str]] | None = None,
    real_n_subjects: int,
    alpha: float,
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for proposing a metric."""
    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name,
        real_n_subjects=real_n_subjects,
        alpha=alpha,
    )

    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        design_header=experiment_class.pretty_print_protocol(),
        experiment_block=experiment.pretty_print(),
        advocating_description=advocating.pretty_print(),
        competing_description=competing.pretty_print(),
        output_columns=_format_columns(experiment_class.output_columns),
        ledger=_format_ledger(ledger or []),
        instruction_format=metric_class.instruction_format(),
    )
    return system_prompt, user_prompt
```

原檔：`upstream/src/prompts/metric_proposal.py`。來源定位：`src/prompts/metric_proposal.py`。

### 6. model_improvement — current source

需要提供：arbiter_guide；arbiter_theory_key；best_k；body_header；candidate.description；candidate.policy_source；candidate.predict_source；delta；desc_block；design_header；domain；entries；estimate_note；experiment_description；experimental_results；fits；header；history_keys_doc；i；idx；instruction_format；it.rationale；k；label；label_str；leaderboard_block；loss_trajectory_block；marker；model_header；obs.metric.metric_source；outcome_line；p.label；parameter_variables；previous_candidate_block；prior_feedback_block；proposal_directive；rationale；rendered；round_theories_block；section_title；suffix；target_idx；target_label；theory.description；theory.policy_source；theory.predict_source；trajectory_block；trajectory_section；v。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

````python
"""Prompt: refine the *model* (predict / policy / parameter ranges) under a
fixed *theory description*.

Used by the `Improver` agent when the arbiter's verdict is `"new_model"`. The
LLM keeps the prose theory verbatim and only regenerates the runnable bits.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.metric import Estimate, fmt_estimate
from src.prompts.interpret_results import ESTIMATE_NOTE, _fmt

if TYPE_CHECKING:
    from src.experiment import Experiment
    from src.feedback import PriorIteration
    from src.observation import Observation
    from src.promptable import Promptable
    from src.theory import Theory


SYSTEM_PROMPT = """\
You are a renowned cognitive scientist and an expert Python programmer.

Your job is to propose a NEW model instantiation of an EXISTING theory, given \
arbiter feedback on the previous instantiation. The theory's prose claim is \
fixed — you are NOT redefining the theory. You are regenerating only the \
runnable bits: the `predict` function, the `policy` function, and the \
`parameters` ranges. The newly proposed model should display human-like \
behavior when simulated on experiments in the {domain} domain.

The goal of the model improvement process is to SURFACE theories that are EXPERIMENT-INVARIANT: that is,\
theories that explain data across multiple experiments. \

If your model fails to compile or behaves badly, you may receive feedback and \
have to propose another instantiation. Iterate until accepted.

If you think the failure to capture human behavior is due to arbiter feedback \
that is inaccurate or unhelpful, you can propose a new model instance that \
ignores the feedback, but you must provide rationale for why you are ignoring \
it and how your proposal overcomes the identified mechanistic failures.

## ACCEPT GATE & LOSS TRAJECTORY — HOW THE LOOP HANDLES YOUR EDITS
This propose-loop has a programmatic accept gate: after every iteration the \
candidate's `aggregate_loss` is compared against the running-best loss; \
strict improvement -> ACCEPTED (the candidate becomes the new running-best \
base); otherwise -> REJECTED (the candidate is discarded and the base is \
unchanged). You do NOT need to manually "revert" a regressed edit — the gate \
already does that for you.

The block rendered below as `## PREVIOUS CANDIDATE (this loop)` is ALWAYS the \
running-best (last ACCEPTED) candidate, NEVER your most recent attempt if it \
was rejected. So:
  * Treat `## PREVIOUS CANDIDATE` as a known-good base. Build on it.
  * The `## LOSS TRAJECTORY` block tags every iteration ACCEPTED or REJECTED. \
Use this as ground truth on which past critic advice actually moved the loop \
forward and which didn't.
  * The `## PRIOR FEEDBACK ITERATIONS` block annotates each prior critique \
with the same ACCEPTED/REJECTED tag of the candidate it elicited. Down-weight \
critic advice whose previous candidates were REJECTED, and reinforce / extend \
advice whose candidates were ACCEPTED.
  * Treat the best ACCEPTED iteration's loss as a soft floor — the next edit \
should plausibly land at-or-below it, otherwise the gate will reject your \
attempt and the base stays put.

{estimate_note}

## PARAMETER NOTATION
`parameters` is a JSON object mapping each parameter name (snake_case string) \
to a *string* value that specifies its domain. Every value MUST be a string — \
never a bare list, number, tuple, or expression. Use exactly one of these \
notations per parameter:

1. Continuous interval — square brackets, two numeric bounds:
   "[min, max]"
   Examples: "[0, 1]", "[1.0, 10.0]", "[10, 1000]"

2. Discrete set — curly braces, comma-separated values:
   "{{v1, v2, ...}}"
   Example: "{{1, 2}}"

3. Vector of intervals whose length is set by the experiment — a bracketed \
tuple repeated by a symbolic length variable:
   "[(min, max)] * length_var"
   Example: "[(0, 1)] * n_features"

4. Symbolic reference — a bare variable name (no brackets, no angle brackets), \
used when the parameter takes its value from an experiment-defined constant \
rather than a range:
   "variable_name"
   Example: "n_features"

Rules:
- Do not use parentheses for intervals; square brackets only. Tuples `(a, b)` \
are reserved for the vector-of-intervals notation in (3).
- Do not mix notations within a single value (e.g., no "[0, 1] or {{2, 3}}").
- Do not quote numbers inside the notation (write "[0, 1]", not "['0', '1']").
- Every parameter referenced by `predict` or `policy` must appear as a key in \
`parameters`, and vice versa.
- Notations 3 and 4 may ONLY reference the experiment-defined symbolic \
identifiers listed under "ALLOWED SYMBOLIC IDENTIFIERS" below. Do not invent \
new identifier names. If a parameter's shape doesn't fit any of those \
variables, fall back to a literal interval (notation 1) or discrete set \
(notation 2). Use these names so the model adapts to any experiment in \
this domain instead of hardcoding shapes.

## ALLOWED SYMBOLIC IDENTIFIERS (for notations 3 and 4 above)
{parameter_variables}

## AVAILABLE IMPORTS inside `predict` and `policy`
- numpy as np
- pandas as pd
- scipy and its submodules
- torch and torch.nn.functional as F
- sklearn and its submodules
- math, random, and other standard Python libraries

## RUNTIME CONTRACT (function signatures and argument shapes)
`predict(parameters, state, history) -> np.ndarray`:
- `parameters`: dict[str, value]. One sample drawn from your declared \
`parameters` ranges, applied for the entire subject run.
- `state`: the per-trial input delivered by the experiment (shape is \
domain-specific — see the experiment description above and the `history` key \
list below, which mirrors the per-trial variables carried in `state`). \
Convert to an array with `np.asarray(state)` if you need array ops.
- `history`: dict-of-lists for past trials in this subject's run, NOT a \
list-of-dicts. The per-trial keys are:
{history_keys_doc}
Iterating `for x in history:` iterates the dict KEYS (strings); \
to walk trials index the lists in lock-step, e.g. \
`for i in range(len(next(iter(history.values())))): ...`.
- Returns: 1-D `np.ndarray` of choice probabilities over the experiment's \
discrete action set, summing to 1.

`policy(probs) -> int`:
- Receives the probability vector produced by `predict`.
- Returns: integer index in `[0, len(probs))` identifying the chosen \
action. If you sample with `np.random.choice(..., p=probs)`, normalise \
first (`probs = np.asarray(probs, dtype=np.float64); probs /= probs.sum()`) \
to avoid the "probabilities do not sum to 1" ValueError from float drift.
"""


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}

{design_header}

## ROUND THEORIES
The arbiter compared the two theories below this round. Your job is to \
regenerate ONLY the runnable bits (`predict`, `policy`, `parameters`) of the \
one tagged **TO REVISE**, keeping its description verbatim. The other theory \
is shown for context — it is NOT being changed.

{round_theories_block}
## ARBITER GUIDE
{arbiter_theory_key}{arbiter_guide}
{leaderboard_block}{loss_trajectory_block}
## EXPERIMENTAL RESULTS
{experimental_results}
{previous_candidate_block}{prior_feedback_block}

## IMPLEMENTATION GUARDRAILS
- The parameters should be within the specified ranges.
- The model's predictions should be valid probability distributions (non-negative and sum to 1).
- When converting logits to probabilities via softmax, always use the numerically stable form: subtract the max before exponentiating (`x = x - np.max(x); p = np.exp(x); p /= p.sum()`). A naive `np.exp(x) / np.sum(np.exp(x))` overflows to Inf/NaN for large logits. Alternatively, use `scipy.special.softmax`.


{proposal_directive}
## RESPONSE FORMAT
Return a JSON object with the following fields:
{instruction_format}
"""


def _format_one_round_theory(
    theory: "Theory",
    *,
    idx: int,
    label: str | None,
    is_target: bool,
) -> str:
    """Render one theory in the `## ROUND THEORIES` section.

    Mirrors the arbiter's `THEORY 1` / `THEORY 2` headings (anchored to pi
    labels) so any "Theory N" reference in the arbiter's free-text
    recommendation lands on a concrete subsection here. The target (the
    theory being revised) is tagged **TO REVISE**; the other one is tagged
    `(other theory — context only, NOT revised)` and rendered with the same
    depth (description + predict + policy + parameters) so the LLM can
    reason about the contrast.
    """
    label_str = f"`{label}`" if label else "(no label)"
    if is_target:
        suffix = "**TO REVISE**"
        body_header = (
            "**Description (PRESERVE VERBATIM — do not rewrite the prose):**"
        )
        model_header = (
            "**Previous model instance — REGENERATE `predict`, `policy`, "
            "and `parameters` ranges:**"
        )
    else:
        suffix = "(other theory — context only, NOT revised)"
        body_header = "**Description:**"
        model_header = "**Model instance (shown for context):**"
    return (
        f"### THEORY {idx} — {label_str} {suffix}\n\n"
        f"{body_header}\n{theory.description}\n\n"
        f"{model_header}\n\n"
        f"`predict(parameters, state, history) -> np.ndarray`:\n"
        f"{theory.predict_source}\n\n"
        f"`policy(probs) -> int`:\n{theory.policy_source}\n\n"
        f"`parameters`:\n{_format_parameters(theory.parameters)}\n"
    )


def _format_round_theories(
    target_theory: "Theory",
    *,
    other_theory: "Theory | None",
    labels: tuple[str | None, str | None] | None,
    target_idx: int | None,
) -> str:
    """Render the `## ROUND THEORIES` block: both round theories side by
    side, with the target tagged **TO REVISE**.

    Falls back to the legacy "single theory" view (just the killed theory,
    no THEORY 1/2 framing) when `other_theory` or `target_idx` is missing —
    keeps direct callers of `render` working without forcing them to plumb
    round metadata through.
    """
    target_idx_eff = target_idx if target_idx in (1, 2) else 1
    target_label = labels[target_idx_eff - 1] if labels else None
    target_block = _format_one_round_theory(
        target_theory,
        idx=target_idx_eff,
        label=target_label,
        is_target=True,
    )
    if other_theory is None:
        return target_block + "\n"
    other_idx = 3 - target_idx_eff
    other_label = labels[other_idx - 1] if labels else None
    other_block = _format_one_round_theory(
        other_theory,
        idx=other_idx,
        label=other_label,
        is_target=False,
    )
    blocks = sorted(
        [(target_idx_eff, target_block), (other_idx, other_block)],
        key=lambda x: x[0],
    )
    return "\n---\n\n".join(b for _, b in blocks) + "\n"


def _format_arbiter_theory_key(
    labels: tuple[str | None, str | None] | None,
    target_idx: int | None,
) -> str:
    """Render the THEORY 1 / THEORY 2 -> pi-label lookup key for the arbiter
    guide.

    The arbitration prompt rendered the round's two theories as `THEORY 1`
    and `THEORY 2` (anchored to `pi_1` / `pi_2` labels in that prompt), and
    the arbiter's free-text recommendation refers back to those numeric
    labels. Once the recommendation is forwarded here as `arbiter_guide`
    that anchoring is gone, so we re-emit the key right above the guide
    text. Returns "" (no extra block) when labels aren't supplied — old
    callers stay unchanged.

    The returned string ends in a blank line so it slots in cleanly above
    the guide text in the TEMPLATE.
    """
    if not labels or labels[0] is None or labels[1] is None:
        return ""
    lines = [
        "The arbiter labelled this round's two theories in its recommendation as follows:",
        f"- THEORY 1 = `{labels[0]}`",
        f"- THEORY 2 = `{labels[1]}`",
    ]
    if target_idx in (1, 2):
        target_label = labels[target_idx - 1]
        lines.append(
            f"- The recommendation below acts on THEORY {target_idx} "
            f"(= `{target_label}`)."
        )
    return "\n".join(lines) + "\n\n"


def _format_parameter_variables(variables: dict[str, str]) -> str:
    if not variables:
        return "(none)"
    return "\n".join(f"- {k}: {v}" for k, v in variables.items())


def _format_history_keys(output_columns: dict[str, str]) -> str:
    """Render the per-trial `history` dict keys from the experiment's
    `output_columns`, skipping `subject_id` (which is a DataFrame column
    but not a per-trial history key). Mirrors what `Experiment._reset_history`
    sets up on each subclass so the LLM sees the actual keys available
    inside `predict`.

    Each description is emitted verbatim (no `.lower()`, no "list of past "
    prefix surgery) because `output_columns` descriptions are authored as
    per-trial value captions — turning them into "list of …" phrases would
    mangle full sentences (e.g. `"0 if subject chose A, 1 if subject chose B"`).
    A single header line tells the LLM that each value is a list in trial order.
    """
    keys = [(k, v) for k, v in output_columns.items() if k != "subject_id"]
    if not keys:
        return "  (no per-trial keys declared)"
    lines = [
        "  Each value below is a Python list in trial order; entry `i` is the "
        "value for trial `i`. On the first trial all lists are empty."
    ]
    lines.extend(f"  - `\"{k}\"`: {v}" for k, v in keys)
    return "\n".join(lines)


def _format_parameters(parameters: dict[str, str]) -> str:
    if not parameters:
        return "(none)"
    return "\n".join(f"- {k}: {v}" for k, v in parameters.items())


def _format_other_predictions(obs: "Observation") -> str:
    """Render previously-recorded theory predictions on this Observation's
    metric, one per line, as a calibration reference for the proposer.

    Mirrors the same block shown to the feedback critic so the proposer
    sees the same competitor landscape it will be judged against.
    """
    if not obs.predicted_values:
        return "(none)"
    lines = [
        f"- {p.label}: {fmt_estimate(p.as_estimate())}"
        for p in obs.predicted_values
    ]
    return "\n".join(lines)


def _format_prior_trajectory(
    obs_idx: int,
    real_value: float | None,
    prior_iterations: list["PriorIteration"] | None,
) -> str:
    """Render the per-experiment trajectory of THIS loop's prior candidates.

    The proposer hasn't simulated the next candidate yet, so (unlike the
    feedback prompt) there is no "current" row — we only show iterations
    that have already been critiqued. The most recent entry corresponds to
    the source rendered verbatim under `## PREVIOUS CANDIDATE (this loop)`.
    Each row carries both the point estimate and the between-subject
    variance so a candidate that's drifting in noise (rather than mean) is
    visible in the trace.
    """
    if not prior_iterations:
        return ""
    rows: list[str] = []
    last = len(prior_iterations)
    for k, it in enumerate(prior_iterations, start=1):
        est = it.estimates[obs_idx] if obs_idx < len(it.estimates) else None
        delta = (
            f" (Δ vs real {est.value - real_value:+.4f})"
            if est is not None
            and est.value is not None
            and real_value is not None
            else ""
        )
        suffix = " (most recent)" if k == last else ""
        rows.append(f"  - iter {k}{suffix}: {fmt_estimate(est)}{delta}")
    return "**Previous candidate values (this loop):**\n" + "\n".join(rows)


def _format_observations(
    observations: list["Observation"],
    *,
    prior_iterations: list["PriorIteration"] | None = None,
) -> str:
    """Render a list of Observations as the EXPERIMENTAL RESULTS block.

    For each observation we show:
      - the experimental design (delegated to `experiment.pretty_print()`),
      - the metric (rationale + source),
      - the observed real value,
      - (when `prior_iterations` is non-empty) the per-experiment trajectory
        of this loop's prior candidate values, so the proposer can see how
        its own iterates have moved on this metric and avoid oscillating,
      - the values produced by every other theory previously evaluated
        against this metric, as a calibration reference (same block the
        feedback critic sees).
    """
    if not observations:
        return "(no observations yet)"
    blocks: list[str] = []
    for i, obs in enumerate(observations, start=1):
        trajectory_block = _format_prior_trajectory(
            i - 1, obs.real_value, prior_iterations
        )
        trajectory_section = f"{trajectory_block}\n" if trajectory_block else ""
        block = (
            f"### Experiment {i}\n"
            f"**Design**\n{obs.experiment.pretty_print_design()}\n\n"
            f"**Metric**\n"
            f"```python\n{obs.metric.metric_source}\n```\n\n"
            f"**Observed (real) value:** {fmt_estimate(obs.real_as_estimate())}\n"
            f"{trajectory_section}"
            f"**Other theories' values on this metric (for reference):**\n"
            f"{_format_other_predictions(obs)}"
        )
        blocks.append(block)
    return "\n\n".join(blocks)


def _format_leaderboard_entry(
    label: str,
    theory: "Theory",
    score: float,
    observations: list["Observation"] | None,
) -> str:
    """Render one leaderboard entry as a sub-section.

    Includes the theory's prose description, predict / policy source,
    parameter ranges, overall score, and per-observation `real= … vs this= …`
    fit table — i.e. enough for the LLM to compare its candidate against
    this competitor on the *same* evidence.
    """
    rows: list[str] = []
    for i, obs in enumerate(observations or [], start=1):
        pred = obs.prediction_by_label(label)
        rows.append(
            f"- Experiment {i}: "
            f"real={fmt_estimate(obs.real_as_estimate())} "
            f"vs this={fmt_estimate(pred.as_estimate() if pred is not None else None)}"
        )
    fits = "\n".join(rows) if rows else "(no observations to compare on yet)"
    return (
        f"### `{label}` (overall score: {score:.3f})\n\n"
        f"**Description**\n{theory.description}\n\n"
        f"`predict(parameters, state, history) -> np.ndarray`:\n"
        f"{theory.predict_source}\n\n"
        f"`policy(probs) -> int`:\n{theory.policy_source}\n\n"
        f"`parameters`:\n{_format_parameters(theory.parameters)}\n\n"
        f"**Per-experiment fit (real vs this theory's metric value):**\n"
        f"{fits}\n"
    )


def _format_leaderboard_block(
    leaderboard: list[tuple[str, "Theory", float]] | None,
    observations: list["Observation"] | None,
) -> str:
    """Render the `## THEORY LEADERBOARD` section.

    `leaderboard` is a list of `(label, theory, overall_score)` triples
    chosen by `main._select_leaderboard` per the run-level `LEADERBOARD`
    config (`("none" | "best" | "sample", n)`). Each entry expands into a
    full sub-section (description + predict + policy + parameters +
    per-experiment fits + overall score) so the LLM can compare its
    candidate against concrete prior competitors. Returns `""` when the
    leaderboard is empty.

    The arbiter-killed theory is intentionally absent — it is shown above
    as `## PREVIOUS MODEL INSTANCE` and `main._select_leaderboard` filters
    it out of the leaderboard to avoid duplicating its body.
    """
    if not leaderboard:
        return ""
    entries = "\n\n---\n\n".join(
        _format_leaderboard_entry(label, theory, score, observations)
        for label, theory, score in leaderboard
    )
    return (
        "\n## THEORY LEADERBOARD\n"
        "A small set of prior picked theories shown for reference. "
        "Overall score is in `[0, 1]`, higher = better, computed as "
        "`1 - L2_norm(normalized_per_experiment_distances) / max_L2_norm`. "
        "1.0 means closest to the real value on every experiment+metric "
        "pair; 0.0 means farthest. Each entry below carries the same "
        "depth of detail as the PREVIOUS MODEL INSTANCE above so you can "
        "borrow concrete mechanisms when useful.\n\n"
        f"{entries}\n"
    )


def _format_previous_candidate(
    candidate: "Theory | None",
    *,
    include_description: bool,
    section_title: str = "PREVIOUS CANDIDATE (this loop)",
) -> str:
    """Render the previous in-loop candidate's full body.

    Used by both `model_improvement` and `theory_generation` prompts so the
    LLM can see — verbatim — the source it just tried, rather than
    reconstructing it from the critic's prose. Returns `""` when no
    candidate is given (i.e. on the first iteration of the inner loop).

    `include_description` controls whether the prose description is also
    rendered. The improver already shows the (unchanged) theory description
    above as `## THEORY (UNCHANGED …)` so we omit it there to avoid a
    duplicate; the theory_generator changes the description each iteration
    so it must be included.
    """
    if candidate is None:
        return ""
    desc_block = (
        f"**Description**\n{candidate.description}\n\n"
        if include_description else ""
    )
    rationale = candidate.rationale or "(none)"
    return (
        f"\n## {section_title}\n"
        "The RUNNING-BEST (last ACCEPTED) candidate in this critique loop "
        "— i.e. the source the loop's accept gate kept as the best base so "
        "far. If your most recent attempt was REJECTED by the gate, this "
        "is NOT that attempt; it is the previously-accepted base the gate "
        "rolled back to. Iterate on this source — the next critic feedback "
        "should be applied on top of it.\n\n"
        f"{desc_block}"
        f"`predict(parameters, state, history) -> np.ndarray`:\n"
        f"{candidate.predict_source}\n\n"
        f"`policy(probs) -> int`:\n{candidate.policy_source}\n\n"
        f"`parameters`:\n{_format_parameters(candidate.parameters)}\n\n"
        f"`rationale`: {rationale}\n"
    )


def _format_proposal_directive(previous_candidate: "Theory | None") -> str:
    """Render the `## PROPOSAL` block for the model-improvement prompt.

    Two regimes (mirrors the helper in `theory_generation`, but scoped to
    "model" since the description is fixed in this prompt):
      - First iteration of the loop (`previous_candidate is None`): tell
        the LLM to propose a fresh model instance for the unchanged
        theory description above. There is nothing to edit yet, so a
        "minimal-diff" framing would be a no-op.
      - Subsequent iterations (`previous_candidate is not None`): tell
        the LLM to apply a MINIMAL-DIFF EDIT on the source rendered
        verbatim under `## PREVIOUS CANDIDATE (this loop)`. Rewriting
        `predict` / `policy` end-to-end for a small change wastes tokens
        and tends to introduce regressions; pinning the diff to the
        smallest change that resolves the critic's diagnosis keeps the
        loop converging instead of oscillating across full rewrites.
    """
    if previous_candidate is None:
        return (
            "## PROPOSAL\n"
            "Propose a new model instance for the theory above from scratch. "
            "Keep the theory's prose claim implicit but unchanged — your only "
            "job is to regenerate `predict`, `policy`, and the `parameters` "
            "ranges so that the implementation actually displays the behavior "
            "the theory claims, while faithfully implementing the mechanism "
            "family the arbiter prescribed.\n"
        )
    return (
        "## PROPOSAL — MINIMAL-DIFF EDIT (do NOT rewrite from scratch)\n"
        "The RUNNING-BEST (last ACCEPTED) candidate is shown verbatim "
        "above under `## PREVIOUS CANDIDATE (this loop)`. This is the "
        "base the loop's accept gate is currently keeping; the most "
        "recent critic feedback (see `## PRIOR FEEDBACK ITERATIONS`) "
        "should be applied on top of it. Apply the SMALLEST edit that "
        "addresses the critic's diagnosis while staying inside the "
        "arbiter's prescribed mechanism family:\n"
        "  - Re-emit the previous source verbatim, then change ONLY the "
        "lines needed to address the critic (a parameter range, a "
        "normalization, a softmax temperature, an attention scheme, a "
        "gating term, a buggy indexing line, etc.).\n"
        "  - Keep the theory's prose claim implicit but unchanged, and keep "
        "all unaffected functions, equations, parameter names, and the "
        "overall mechanism intact.\n"
        "  - Do NOT rewrite `predict` / `policy` end-to-end if a few lines "
        "would do, and do NOT switch mechanism families — that is the "
        "arbiter's decision, not yours in this loop.\n"
        "  - Briefly explain the minimal edit in `rationale`.\n"
        "If you genuinely believe a larger rewrite is required, you may do "
        "one, but justify in `rationale` why the minimal-diff path was "
        "insufficient.\n"
    )


def _fmt_loss(loss: float | None) -> str:
    """Render an `aggregate_loss` value compactly. `None` is shown as `n/a`,
    `+inf` as `+inf` (unscorable), everything else with 4 decimals.
    Mirrors the helper in `src/prompts/feedback.py` so both sides of the
    propose-loop format losses the same way."""
    if loss is None:
        return "n/a"
    if loss == float("inf"):
        return "+inf"
    if loss == float("-inf"):
        return "-inf"
    return f"{loss:.4f}"


def _accept_marker(accepted: bool | None) -> str:
    """Render the accept-gate verdict for an iteration. Mirrors the helper
    in `src/prompts/feedback.py` (kept local here to avoid a cycle between
    the two prompt modules)."""
    if accepted is None:
        return "?"
    return "ACCEPTED" if accepted else "REJECTED"


def _format_loss_trajectory_block(
    prior_iterations: list["PriorIteration"] | None,
) -> str:
    """Render the propose-loop's `aggregate_loss` trajectory for the proposer.

    Each row carries `loss` plus the loop's programmatic ACCEPTED /
    REJECTED tag (`loss < accepted_loss` -> ACCEPTED, else REJECTED).
    Unlike the critic's view there is no "current candidate" row — the
    proposer hasn't simulated the next candidate yet. The block ends with
    a one-line summary pointing the proposer at the running-best (last
    ACCEPTED) candidate, which is exactly the source rendered verbatim
    below under `## PREVIOUS CANDIDATE (this loop)`.

    Returns "" on iter 0 (nothing to render).
    """
    if not prior_iterations:
        return ""
    rows: list[str] = []
    accepted_iters: list[tuple[int, float]] = []
    for k, it in enumerate(prior_iterations, start=1):
        rows.append(
            f"- iter {k}: loss={_fmt_loss(it.loss)} "
            f"-> {_accept_marker(it.accepted)}"
        )
        if it.accepted and it.loss != float("inf"):
            accepted_iters.append((k, it.loss))
    if accepted_iters:
        best_k, best_l = min(accepted_iters, key=lambda kl: kl[1])
        best_line = (
            f"\nRunning-best (last ACCEPTED) base: iter {best_k} at loss="
            f"{_fmt_loss(best_l)} — this is the source shown verbatim below "
            f"under `## PREVIOUS CANDIDATE (this loop)`. Push the next "
            f"edit's loss strictly below that floor or the gate will "
            f"reject it."
        )
    else:
        best_line = (
            "\nNo iteration has been ACCEPTED yet by the gate. The source "
            "shown below as `## PREVIOUS CANDIDATE (this loop)` is the "
            "best-so-far attempt; any finite-loss improvement on it will be "
            "auto-accepted."
        )
    return (
        "\n## LOSS TRAJECTORY (this propose-loop)\n"
        "Aggregate loss across iterations of THIS propose-loop "
        "(lower = better, 0 = perfect, `+inf` = unscorable). The "
        "ACCEPTED / REJECTED tag is the loop's programmatic accept-gate "
        "decision — only ACCEPTED candidates have ever been used as the "
        "base for a subsequent iteration. Use this together with PRIOR "
        "FEEDBACK ITERATIONS below to grade which past critic advice "
        "actually paid off.\n\n"
        + "\n".join(rows)
        + best_line
        + "\n"
    )


def _format_prior_feedback(
    prior_iterations: list["PriorIteration"] | None,
) -> str:
    """Render the chronological log of prior critic verdicts, each annotated
    with the accept-gate outcome of the candidate it elicited.

    The proposer needs this in two ways:
      1. The literal prose feedback to address (mostly the most recent one).
      2. A per-iteration ACCEPTED / REJECTED marker so it knows which past
         pieces of advice ended up improving the running best and which
         did not — advice whose candidates were REJECTED should be
         discounted, even when the current critic still pushes in the
         same direction.

    For iter k's "outcome" we look at `prior_iterations[k].accepted` (=
    the next candidate's accept status). For the most recent prior
    critique (the one whose advice the proposer is about to address) the
    next candidate hasn't been built yet — we mark that as PENDING.
    """
    if not prior_iterations:
        return ""
    blocks: list[str] = []
    for i, it in enumerate(prior_iterations, start=1):
        is_last = i == len(prior_iterations)
        if is_last:
            outcome_line = (
                f"**Outcome of this advice:** iter {i} candidate loss="
                f"{_fmt_loss(it.loss)} -> next candidate accept-status=PENDING "
                f"(this is the advice you are addressing now)."
            )
            header = f"### Iteration {i} (most recent — address this)"
        else:
            next_it = prior_iterations[i]
            marker = _accept_marker(next_it.accepted)
            outcome_line = (
                f"**Outcome of this advice:** iter {i} candidate loss="
                f"{_fmt_loss(it.loss)} -> iter {i + 1} candidate loss="
                f"{_fmt_loss(next_it.loss)} -> the gate marked it {marker}."
            )
            header = f"### Iteration {i}"
        blocks.append(f"{header}\n{it.rationale}\n\n{outcome_line}")
    rendered = "\n\n".join(blocks)
    return (
        "\n## PRIOR FEEDBACK ITERATIONS\n"
        "The critic's verdicts on each previous in-loop candidate, in "
        "order. Each block ends with an **Outcome of this advice** line "
        "saying whether the candidate the proposer produced AFTER this "
        "advice was ACCEPTED (loss strictly beat the running best) or "
        "REJECTED (the gate discarded it). Address the most recent "
        "iteration's feedback in your next edit, but down-weight past "
        "advice whose candidates were REJECTED.\n\n"
        f"{rendered}\n"
    )


def render(
    *,
    experiment_class: type["Experiment"],
    theory: "Theory",
    response_schema: type["Promptable"],
    arbiter_guide: str,
    arbiter_theory_labels: tuple[str | None, str | None] | None = None,
    arbiter_target_idx: int | None = None,
    other_theory: "Theory | None" = None,
    observations: list["Observation"] | None = None,
    previous_candidate: "Theory | None" = None,
    leaderboard: list[tuple[str, "Theory", float]] | None = None,
    prior_iterations: list["PriorIteration"] | None = None,
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for proposing a new Model under
    an existing Theory.

    `arbiter_theory_labels` is the `(theory_1_pi_label, theory_2_pi_label)`
    pair the arbiter saw under its `THEORY 1` / `THEORY 2` headings; when
    provided, a small lookup key is rendered above `arbiter_guide` so the
    LLM can resolve any numeric "Theory 1 / Theory 2" references in the
    arbiter's free-text recommendation back to concrete pi labels.
    `arbiter_target_idx` (1 or 2) flags which of those theories the
    recommendation acts on.

    `other_theory` is the round's NON-target theory. When provided
    (alongside `arbiter_theory_labels` + `arbiter_target_idx`), the
    `## ROUND THEORIES` block renders both theories side by side under
    `THEORY 1` / `THEORY 2` headings — the target tagged **TO REVISE** —
    so any numeric references in the arbiter's recommendation point at a
    concrete subsection here. When omitted, the block degrades to a single
    theory view (target only).

    `previous_candidate`, when provided, is the most recent in-loop attempt
    rendered verbatim under `## PREVIOUS CANDIDATE (this loop)` so the LLM
    can iterate on its own source rather than reconstructing it from the
    critic's prose feedback. Pass `None` on the first iteration.

    `theory` carries both the prose description (preserved verbatim in the
    prompt) and the previous model instance (predict/policy/parameters)
    shown as the "previous instantiation" the LLM should improve on.

    `observations` is the per-experiment evidence the new model must
    explain — typically every Observation across every Round in the pool
    (regardless of which pi proposed each). The block is auto-formatted via
    `_format_observations`: experimental design → metric → real value →
    (when `prior_iterations` is given) this loop's prior candidate
    trajectory → other theories' values on the same metric, per
    observation.

    `response_schema` is the Pydantic class the LLM's output is parsed into
    (typically `Model` from `src/theory.py`); its `instruction_format()`
    produces the field-list block at the bottom of the user prompt.

    `prior_iterations` is the chronological history of this propose-loop as
    `PriorIteration(rationale, estimates, loss, accepted)` entries. The
    estimate list is in the SAME order as `observations` so the
    EXPERIMENTAL RESULTS block can render a per-experiment trajectory;
    the `loss` and `accepted` fields together power both the
    `## LOSS TRAJECTORY` block (one row per iteration with the
    ACCEPTED / REJECTED tag from the loop's accept gate) and the
    "Outcome of this advice" line in `## PRIOR FEEDBACK ITERATIONS` so
    the proposer can down-weight past critiques whose candidates were
    REJECTED by the gate.
    """
    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name,
        parameter_variables=_format_parameter_variables(
            experiment_class.parameter_variables
        ),
        history_keys_doc=_format_history_keys(experiment_class.output_columns),
        estimate_note=ESTIMATE_NOTE,
    )

    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        design_header=experiment_class.pretty_print_protocol(),
        round_theories_block=_format_round_theories(
            theory,
            other_theory=other_theory,
            labels=arbiter_theory_labels,
            target_idx=arbiter_target_idx,
        ),
        arbiter_guide=arbiter_guide,
        arbiter_theory_key=_format_arbiter_theory_key(
            arbiter_theory_labels, arbiter_target_idx
        ),
        leaderboard_block=_format_leaderboard_block(leaderboard, observations),
        loss_trajectory_block=_format_loss_trajectory_block(prior_iterations),
        experimental_results=_format_observations(
            observations or [], prior_iterations=prior_iterations
        ),
        previous_candidate_block=_format_previous_candidate(
            previous_candidate, include_description=False
        ),
        prior_feedback_block=_format_prior_feedback(prior_iterations),
        proposal_directive=_format_proposal_directive(previous_candidate),
        instruction_format=response_schema.instruction_format(),
    )
    return system_prompt, user_prompt
````

原檔：`upstream/src/prompts/model_improvement.py`。來源定位：`src/prompts/model_improvement.py`。

### 7. theory_generation — current source

需要提供：arbiter_guide；arbiter_theory_key；design_header；diversity_requirement；domain；estimate_note；experiment_description；experimental_results；history_keys_doc；instruction_format；k；leaderboard_block；loss_trajectory_block；parameter_variables；previous_candidate_block；previous_models；prior_feedback_block；proposal_directive；target；v。

用途：含渲染函式的提示模組。原文範圍：完整模組；相依資料型別與執行系統仍需官方專案。

```python
from __future__ import annotations

from typing import TYPE_CHECKING

from src.prompts.interpret_results import ESTIMATE_NOTE
from src.prompts.model_improvement import (
    _format_arbiter_theory_key,
    _format_history_keys,
    _format_leaderboard_block,
    _format_loss_trajectory_block,
    _format_observations,
    _format_previous_candidate,
    _format_prior_feedback,
)

if TYPE_CHECKING:
    from src.experiment import Experiment
    from src.feedback import PriorIteration
    from src.observation import Observation
    from src.promptable import Promptable
    from src.theory import Theory

SYSTEM_PROMPT = """\
You are a renowned cognitive scientist and an expert Python programmer.

Your job is to propose a new theory and its model instantiation in the {domain} domain \
based on the feedback provided by an arbiter. \
The feedback contains diagnoses of mechanistic failures of the previous \
theory along with suggestions for a new \
theory family that overcomes those failures. \
The newly proposed theory and model should display human-like behavior when simulated on experiment(s). \

The goal of the theory generation process is to SURFACE theories that are EXPERIMENT-INVARIANT: that is,\
theories that explain data across the majority of experiments. \

You will see a list of theories that have been proposed in the past but you should \
only use them as inspiration and not to choose from them. Propose a new theory that is \
different. \

If they fail to do so, you will receive feedback on their performance \
on the same experiment(s) and you will have to propose another new theory and \
model that meet the requirements, iterating until you succeed.

If you think the failure to capture human behavior is due to arbiter feedback \
that is inaccurate or unhelpful, you can propose a new theory and model that ignore the feedback, \
but you must provide rationale for why you are ignoring it and how your proposal overcomes the identified mechanistic failures.

## ACCEPT GATE & LOSS TRAJECTORY — HOW THE LOOP HANDLES YOUR EDITS
This propose-loop has a programmatic accept gate: after every iteration the \
candidate's `aggregate_loss` is compared against the running-best loss; \
strict improvement -> ACCEPTED (the candidate becomes the new running-best \
base); otherwise -> REJECTED (the candidate is discarded and the base is \
unchanged). You do NOT need to manually "revert" a regressed edit — the gate \
already does that for you.

The block rendered below as `## PREVIOUS CANDIDATE (this loop)` is ALWAYS the \
running-best (last ACCEPTED) candidate, NEVER your most recent attempt if it \
was rejected. So:
  * Treat `## PREVIOUS CANDIDATE` as a known-good base. Build on it.
  * The `## LOSS TRAJECTORY` block tags every iteration ACCEPTED or REJECTED. \
Use this as ground truth on which past critic advice actually moved the loop \
forward and which didn't.
  * The `## PRIOR FEEDBACK ITERATIONS` block annotates each prior critique \
with the same ACCEPTED/REJECTED tag of the candidate it elicited. Down-weight \
critic advice whose previous candidates were REJECTED, and reinforce / extend \
advice whose candidates were ACCEPTED.
  * Treat the best ACCEPTED iteration's loss as a soft floor — the next edit \
should plausibly land at-or-below it, otherwise the gate will reject your \
attempt and the base stays put.

{estimate_note}

## PARAMETER NOTATION
`parameters` is a JSON object mapping each parameter name (snake_case string) \
to a *string* value that specifies its domain. Every value MUST be a string — \
never a bare list, number, tuple, or expression. Use exactly one of these \
notations per parameter:

1. Continuous interval — square brackets, two numeric bounds:
   "[min, max]"
   Examples: "[0, 1]", "[1.0, 10.0]", "[10, 1000]"

2. Discrete set — curly braces, comma-separated values:
   "{{v1, v2, ...}}"
   Example: "{{1, 2}}"

3. Vector of intervals whose length is set by the experiment — a bracketed \
tuple repeated by a symbolic length variable:
   "[(min, max)] * length_var"
   Example: "[(0, 1)] * n_features"

4. Symbolic reference — a bare variable name (no brackets, no angle brackets), \
used when the parameter takes its value from an experiment-defined constant \
rather than a range:
   "variable_name"
   Example: "n_features"

Rules:
- Do not use parentheses for intervals; square brackets only. Tuples `(a, b)` are reserved for the vector-of-intervals notation in (3).
- Do not mix notations within a single value (e.g., no "[0, 1] or {{2, 3}}").
- Do not quote numbers inside the notation (write "[0, 1]", not "['0', '1']").
- Every parameter referenced by `predict` or `policy` must appear as a key in \
`parameters`, and vice versa.
- Notations 3 and 4 may ONLY reference the experiment-defined symbolic \
identifiers listed under "ALLOWED SYMBOLIC IDENTIFIERS" below. Do not invent \
new identifier names. If a parameter's shape doesn't fit any of those \
variables, fall back to a literal interval (notation 1) or discrete set \
(notation 2). Use these names so the model adapts to any experiment in \
this domain instead of hardcoding shapes.

## ALLOWED SYMBOLIC IDENTIFIERS (for notations 3 and 4 above)
{parameter_variables}

## AVAILABLE IMPORTS inside `predict` and `policy`
- numpy as np
- pandas as pd
- scipy and its submodules
- torch and torch.nn.functional as F
- sklearn and its submodules
- math, random, and other standard Python libraries

## RUNTIME CONTRACT (function signatures and argument shapes)
`predict(parameters, state, history) -> np.ndarray`:
- `parameters`: dict[str, value]. One sample drawn from your declared \
`parameters` ranges, applied for the entire subject run.
- `state`: the per-trial input delivered by the experiment (shape is \
domain-specific — see the experiment description above and the `history` key \
list below, which mirrors the per-trial variables carried in `state`). \
Convert to an array with `np.asarray(state)` if you need array ops.
- `history`: dict-of-lists for past trials in this subject's run, NOT a \
list-of-dicts. The per-trial keys are:
{history_keys_doc}
Iterating `for x in history:` iterates the dict KEYS (strings); \
to walk trials index the lists in lock-step, e.g. \
`for i in range(len(next(iter(history.values())))): ...`.
- Returns: 1-D `np.ndarray` of choice probabilities over the experiment's \
discrete action set, summing to 1.

`policy(probs) -> int`:
- Receives the probability vector produced by `predict`.
- Returns: integer index in `[0, len(probs))` identifying the chosen \
action. If you sample with `np.random.choice(..., p=probs)`, normalise \
first (`probs = np.asarray(probs, dtype=np.float64); probs /= probs.sum()`) \
to avoid the "probabilities do not sum to 1" ValueError from float drift.
"""


TEMPLATE = """\
## EXPERIMENTAL DOMAIN
{experiment_description}

{design_header}

## ARBITER GUIDE
{arbiter_theory_key}{arbiter_guide}
{leaderboard_block}{loss_trajectory_block}
## EXPERIMENTAL RESULTS
{experimental_results}
{previous_candidate_block}{prior_feedback_block}

## IMPLEMENTATION GUARDRAILS
- The parameters should be within the specified ranges.
- The model's predictions should be valid probability distributions (non-negative and sum to 1).
- When converting logits to probabilities via softmax, always use the numerically stable form: subtract the max before exponentiating (`x = x - np.max(x); p = np.exp(x); p /= p.sum()`). A naive `np.exp(x) / np.sum(np.exp(x))` overflows to Inf/NaN for large logits. Alternatively, use `scipy.special.softmax`.


{proposal_directive}
## RESPONSE FORMAT
Return a JSON object with the following fields:
{instruction_format}
"""
# TODO PREVIOUS MODEL INSTANCES
# {previous_models}
# DIVERSITY REQUIREMENT
# {diversity_requirement}


def _format_parameter_variables(variables: dict[str, str]) -> str:
    if not variables:
        return "(none)"
    return "\n".join(f"- {k}: {v}" for k, v in variables.items())


def _format_proposal_directive(
    previous_candidate: "Theory | None",
    *,
    target: str,
) -> str:
    """Render the `## PROPOSAL` block.

    Two regimes:
      - First iteration of the loop (`previous_candidate is None`): tell
        the LLM to propose from scratch (the original behaviour). There
        is nothing to edit yet, so a "minimal-diff" framing would be a
        no-op.
      - Subsequent iterations (`previous_candidate is not None`): tell
        the LLM to apply a MINIMAL-DIFF EDIT on the source rendered
        verbatim under `## PREVIOUS CANDIDATE (this loop)`. Rewriting the
        whole `predict` / `policy` for a small parameter or equation
        change wastes ~2k tokens per iteration and tends to introduce
        regressions. Pinning the diff to the smallest change that resolves
        the critic's diagnosis keeps the loop converging instead of
        oscillating across full rewrites.

    `target` controls the noun used in the directive
    (`"theory"` for theory_generation, `"model"` for model_improvement) so
    the same helper renders well in both prompts.
    """
    if previous_candidate is None:
        return (
            f"## PROPOSAL\n"
            f"Propose a novel {target} from scratch based on all the information "
            f"available, faithfully implementing the mechanism family the arbiter "
            f"prescribed above. Do NOT simply reuse anything generated in past "
            f"rounds.\n"
        )
    return (
        "## PROPOSAL — MINIMAL-DIFF EDIT (do NOT rewrite from scratch)\n"
        "The RUNNING-BEST (last ACCEPTED) candidate is shown verbatim "
        "above under `## PREVIOUS CANDIDATE (this loop)`. This is the "
        "base the loop's accept gate is currently keeping; the most "
        "recent critic feedback (see `## PRIOR FEEDBACK ITERATIONS`) "
        "should be applied on top of it. Apply the SMALLEST edit that "
        "addresses the critic's diagnosis while staying inside the "
        "arbiter's prescribed mechanism family:\n"
        "  - Re-emit the previous source verbatim, then change ONLY the lines "
        "needed to address the critic (a parameter range, a normalization, a "
        "softmax temperature, an attention scheme, a gating term, a buggy "
        "indexing line, etc.).\n"
        "  - Keep all unaffected functions, equations, parameter names, and the "
        "overall mechanism intact.\n"
        "  - Do NOT rewrite `predict` / `policy` end-to-end if a few lines would "
        "do, and do NOT switch mechanism families — that is the arbiter's "
        "decision, not yours in this loop.\n"
        "  - Briefly explain the minimal edit in `rationale`.\n"
        "If you genuinely believe a larger rewrite is required, you may do one, "
        "but justify in `rationale` why the minimal-diff path was insufficient.\n"
    )


def render(
    *,
    experiment_class: type["Experiment"],
    response_schema: type["Promptable"],
    arbiter_guide: str,
    arbiter_theory_labels: tuple[str | None, str | None] | None = None,
    arbiter_target_idx: int | None = None,
    observations: list["Observation"] | None = None,
    previous_candidate: "Theory | None" = None,
    leaderboard: list[tuple[str, "Theory", float]] | None = None,
    prior_iterations: list["PriorIteration"] | None = None,
) -> tuple[str, str]:
    """Returns (system_prompt, user_prompt) for proposing a brand-new Theory.

    `arbiter_theory_labels` is the `(theory_1_pi_label, theory_2_pi_label)`
    pair the arbiter saw under its `THEORY 1` / `THEORY 2` headings; when
    provided, a small lookup key is rendered above `arbiter_guide` so the
    LLM can resolve any numeric "Theory 1 / Theory 2" references in the
    arbiter's free-text recommendation back to concrete pi labels.
    `arbiter_target_idx` (1 or 2) flags which of those theories the
    recommendation acts on (i.e. the one being replaced wholesale here).

    `previous_candidate`, when provided, is the most recent in-loop attempt
    rendered verbatim under `## PREVIOUS CANDIDATE (this loop)` so the LLM
    can iterate on its own source rather than reconstructing it from the
    critic's prose feedback. Pass `None` on the first iteration.

    `observations` is the empirical evidence the new theory must explain —
    typically every `Observation` in the latest Round. Each is rendered as
    (experimental design, metric, real value, this loop's prior candidate
    trajectory when `prior_iterations` is given, other theories' values on
    the same metric) via `_format_observations` (shared with
    `model_improvement`).

    `response_schema` is the Pydantic class the LLM's output will be parsed
    into (typically `Theory` itself); its `instruction_format()` produces the
    field-list block at the bottom of the user prompt.

    `prior_iterations` is the chronological history of this propose-loop as
    `PriorIteration(rationale, estimates, loss, accepted)` entries. The
    estimate list is in the SAME order as `observations` so the
    EXPERIMENTAL RESULTS block can render a per-experiment trajectory;
    the `loss` and `accepted` fields together power both the
    `## LOSS TRAJECTORY` block (one row per iteration with the
    ACCEPTED / REJECTED tag from the loop's accept gate) and the
    "Outcome of this advice" line in `## PRIOR FEEDBACK ITERATIONS` so
    the proposer can down-weight past critiques whose candidates were
    REJECTED by the gate.
    """
    system_prompt = SYSTEM_PROMPT.format(
        domain=experiment_class.name,
        parameter_variables=_format_parameter_variables(
            experiment_class.parameter_variables
        ),
        history_keys_doc=_format_history_keys(experiment_class.output_columns),
        estimate_note=ESTIMATE_NOTE,
    )

    user_prompt = TEMPLATE.format(
        experiment_description=experiment_class.description,
        design_header=experiment_class.pretty_print_protocol(),
        arbiter_guide=arbiter_guide,
        arbiter_theory_key=_format_arbiter_theory_key(
            arbiter_theory_labels, arbiter_target_idx
        ),
        leaderboard_block=_format_leaderboard_block(leaderboard, observations),
        loss_trajectory_block=_format_loss_trajectory_block(prior_iterations),
        experimental_results=_format_observations(
            observations or [], prior_iterations=prior_iterations
        ),
        previous_candidate_block=_format_previous_candidate(
            previous_candidate, include_description=True
        ),
        prior_feedback_block=_format_prior_feedback(prior_iterations),
        proposal_directive=_format_proposal_directive(
            previous_candidate, target="theory"
        ),
        instruction_format=response_schema.instruction_format(),
    )
    return system_prompt, user_prompt
```

原檔：`upstream/src/prompts/theory_generation.py`。來源定位：`src/prompts/theory_generation.py`。

[論文 PDF](paper.pdf) · [arXiv 論文](https://arxiv.org/html/2606.26448v1) · [官方程式固定版本](https://github.com/akjagadish/autocog/tree/56ed3c9c389a5309fc245c8d3976add7d277bd4b) · [逐檔來源與授權](../../sources.json)
