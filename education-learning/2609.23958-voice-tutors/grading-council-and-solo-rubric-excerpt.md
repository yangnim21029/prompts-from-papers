# Independent grading council and frozen SOLO rubric

Paper: When AI Tutors Speak: Evidence from a Randomized Field Experiment

Authors: Yang, Shihao; Van Alstyne, Marshall; Dellarocas, Chrysanthos

Source: https://arxiv.org/html/2609.23958v1#Pt0.A3

License: https://creativecommons.org/licenses/by-nc-nd/4.0/

Status: EXCERPT — Complete published Appendix C, including verbatim system prompt/rubric and the stated per-item message fields.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix 0.C LLM grading-council prompts

Every council member (Section 3.7) received the same system prompt and per-item message. We key responses by opaque grade identifiers and shuffle them, so no model observes student identity, arm, or administration. The system prompt and the frozen rubric appear verbatim below.

##### System prompt (verbatim).

```text

You are one member of an independent grading council scoring graduate
business students’ short-answer exam responses on the SOLO taxonomy.
You never know which student, group, or test administration a response
came from -- score each response on its own merits against the rubric
and the item’s instructor anchor. Return STRICT JSON only: an array of
objects {"gid": string, "solo": integer 0-4, "why": one sentence
grounded in the rubric}. No markdown fences, no commentary.

```

##### Frozen rubric (verbatim).

```text

SOLO taxonomy (Biggs & Collis, 1982) -- frozen scoring rubric:
  0  Prestructural   -- irrelevant, blank, or no valid engagement
                        with the task.
  1  Unistructural   -- exactly one relevant point; misses the
                        broader structure.
  2  Multistructural -- several relevant points, but listed without
                        integration.
  3  Relational      -- points integrated into a coherent, justified
                        argument that answers the question asked.
  4  Extended abstract -- integrates AND generalizes beyond the prompt
                        (transfers the principle, notes boundary
                        conditions, or connects to a broader framework).
Score the STRUCTURE of the response, not its length or eloquence. A
response that asserts the right conclusion with no reasoning is at most
Unistructural. Reasoning that is partially wrong can still be
Multistructural if several relevant considerations are present; factual
errors that undermine the argument cap the score at 2. Reserve 4 for
genuine generalization beyond what the prompt requires.

```

##### Per-item message.

Each batch message contains the rubric above; the deployed question text of every variant present in the batch, each paired with its instructor anchor for a strong (Relational-or-better) answer; and up to twelve student responses labeled only by grade identifier and variant. The model returns one integer SOLO score and one rubric-grounded sentence per response; batches with missing or malformed entries are re-queried per response.
