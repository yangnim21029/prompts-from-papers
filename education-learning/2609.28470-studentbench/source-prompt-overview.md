# Prompt text used by released conditions

Each `.txt` file is named by the exact prompt-version identifier stored in `student.json`.
Verbal main-leaderboard AI tasks all use `gre.verbal.plan.lean.v2.txt` and
`gre.verbal.tutor.lean.v2.txt`. Quant main AI tasks use the lean-v3 pair; the mid-v3 and max-v3
files are retained because the separately labeled Quant prompt-research data reference them.

The filename without `.txt` is the join key. These are prompt source files, not rendered
per-student prompts: the application combines them with the student-specific pre-test context.
