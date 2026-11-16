# AI essay grader system prompt and six scoring dimensions

Paper: Experimental Evidence on the Learning Impact of Generative AI

Authors: Contractor, Zara; Reyes, Germán

Source: https://arxiv.org/html/2607.08849v2#A2.SS4\par

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Published system prompt and dimension descriptions; NOT the complete API request. Two required calibration essays, their scores/rationales, and the assembled user message are described but not supplied verbatim.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

### B.4 \parAI Essay Grading

We complement our human grading with AI-generated scores to provide an independent assessment of essay quality. We use Anthropic’s Claude Fable 5.1 to grade each essay on the same five rubric dimensions plus the overall quality rating, using the same 0–10 scale as the Prolific graders.

For each essay, we make six separate API calls—one per grading dimension—to avoid cross-contamination between scores. Each call includes a system prompt establishing the grading context, a description of the dimension, two calibration essays with their suggested scores and rationales for that dimension, and the student essay to be graded. The calibration essays, scores, and rationales are the ones shown to human graders during training, ensuring that human and AI graders share a common scoring anchor. We ask the model for a brief justification followed by an integer score on the 0–10 scale.

The system prompt is as follows:

You are grading essays for a university research study on the determinants of learning. The essays were written by college students, who were given 35 minutes to learn about a topic and respond to a prompt. Each essay is approximately 300--500 words long. Grade each essay on a 0--10 scale. Use the two example essays, their suggested scores, and their rationales to calibrate your standards, and keep those standards consistent across essays. You may use your own knowledge to verify facts.

For each dimension, the user prompt includes the dimension name and a description of what the dimension measures. The descriptions are as follows:

Accuracy of Content. Evaluate the factual correctness and depth of understanding demonstrated in the essay. Consider whether key concepts are accurately described, whether technical details are correct, and whether the student shows genuine comprehension of the topic.

Use of Evidence &

Examples. Assess whether the essay draws on evidence from the reading the students were given. Consider how specific and well-integrated the references are.

Relevance to the Prompt. Measure whether the essay directly addresses the prompt requirements. Consider whether all parts of the prompt are addressed and whether the essay stays focused throughout.

Organization and Structure. Evaluate the essay’s organization, clarity of argument flow, and coherence. Consider whether there is a clear introduction, body, and conclusion, and whether transitions between ideas are smooth.

Writing Style and Clarity. Assess the clarity, readability, grammar, and language precision of the essay. Consider vocabulary, sentence variety, and overall polish of the writing.

Overall Essay Quality. Provide a holistic assessment of the essay’s overall quality. Consider all previous dimensions together: accuracy, evidence, relevance, structure, and writing style.

The prompt also includes the two calibration essays, the essay prompt they answer, and their suggested scores and rationales for the relevant dimension. After presenting the calibration material, the prompt provides the student’s assigned topic, the exact prompt the student was shown in that session, and the essay text. Empty essays, or those with fewer than 20 characters, are skipped and recorded as missing without querying the model.
