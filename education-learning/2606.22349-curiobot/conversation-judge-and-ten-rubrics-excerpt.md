# Conversation judge and ten detailed scoring rubrics

Paper: Curiosity as Linguistic Intervention: Using LLM Tutoring Dialogues to Influence Exploratory Learning Behavior

Authors: Ganganath, Gevindu; Bolonghege, Pasindu; Lyu, Qianru; Varakantham, Pradeep; Kandappu, Thivya

Source: https://arxiv.org/html/2606.22349v1#A3

License: https://creativecommons.org/licenses/by-nc-nd/4.0/

Status: EXCERPT — All published judge instructions and detailed ten-dimension rubrics. The source uses an explicit insertion placeholder for the rubric, retained verbatim.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix C LLM-as-a-Judge

Scoring Prompt

```text
You are an expert evaluator assessing AI tutoring conversations. Your task is to assess the quality of student learning behaviour and tutor instructional behaviour as observed in transcripts. Score the given transcripts across 10 dimensions: 4 student-side and 6 tutor-side. Each dimension uses a 7-point Likert scale. Scores must be grounded in observable evidence - not inferred intent. Score each of the 9 transcripts independently, complete isolation.

CRITICAL DISTINCTIONS:
- A student answering a tutor’s direct question is REACTIVE and does NOT count as explorative or agentive behavior.
- A student posing an unprompted question, volunteering a connection, or extending the topic themselves is PROACTIVE.
- Do not conflate engagement (staying in the conversation) with agency (driving the conversation).

STUDENT-SIDE DIMENSIONS
Evaluate what the STUDENT says and does. Focus on student turns.

FILLER RESPONSE RULE — MANDATORY:
When scoring, completely disregard any student turn consisting primarily of fillers: "yes", "no", "ok", "okay", "sure", "please go ahead", "go on", "np", "got it", "sounds good", "alright", "makes sense", "right", "mm-hmm", "I see", "cool", or any equivalent zero-content acknowledgment. Treat these turns as non-existent. A conversation where the student produces only fillers must score 1.

<All the dimenions come here>

INPUT FORMAT

VARIANT A

Transcript A1 — Filename: FILENAME_A1
<transcript_a1>
…
</transcript_a1>

Transcript A2 — Filename: <FILENAME_A2>
<transcript_a2>
…
</transcript_a2>

Transcript A3 — Filename: <FILENAME_A3>
<transcript_a3>
…
</transcript_a3>

VARIANT B

Transcript B1 — Filename: <FILENAME_B1>
<transcript_b1>
…
</transcript_b1>

Transcript B2 — Filename: <FILENAME_B2>
<transcript_b2>
…
</transcript_b2>

Transcript B3 — Filename: <FILENAME_B3>
<transcript_b3>
…
</transcript_b3>

OUTPUT FORMAT

Return a single JSON object with the structure below. All averages rounded to 2 decimal places.

{"evaluations": [
{
"variant": "VARIANT_A",
"filename": FILENAME_A1,
"student_side": {
"L1": { "score": X, "rationale": "…" },
"L2": { "score": X, "rationale": "…" },
"L3": { "score": X, "rationale": "…" },
"L4": { "score": X, "rationale": "…" }
},
"tutor_side": {
"T1": { "score": X, "rationale": "…" },
"T2": { "score": X, "rationale": "…" },
"T3": { "score": X, "rationale": "…" },
"T4": { "score": X, "rationale": "…" },
"T5": { "score": X, "rationale": "…" },
"T6": { "score": X, "rationale": "…" }
},
"notes": "…"
},
…
]
}
```


## Appendix G Detailed Evaluation Criteria

### L1: Explorative Questions

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | None | No self-generated questions across the conversation. |
| 2 | Clarificatory only | Self-generated questions appear, but all are requests for re-explanation of something already stated. |
| 3 | Surface only | Questions appear in a minor share of substantive turns; all stay within the tutor-set topic with no extension. |
| 4 | Occasional exploratory | At least one question is genuinely exploratory (probes mechanism, implication, or edge case), but exploratory questions remain rare relative to the student’s substantive turns. |
| 5 | Recurring exploratory | A meaningful share of substantive turns include exploratory questions; at least one meaningfully extends the topic beyond the tutor’s framing. |
| 6 | Sustained inquiry | A substantial share of substantive turns include exploratory questions; together they form a developing curiosity thread across the conversation. |
| 7 | Self-directed inquiry | Exploratory questions are pervasive across the student’s substantive turns and shape the conversation’s trajectory; the tutor responds to the student’s intellectual agenda. |

Table 5: 
Rubric for L_{1}.

Prompt L_{1}

```text
Only unprompted, student-originated questions count. Reply-questions that merely respond to a tutor prompt (e.g., tutor:“What do you think causes X?” → student: “Is it Y?”) are reactive and do NOT count.

Two things to weigh together:

Frequency: share of the student’s substantive turns that include a self-generated question

Quality: whether questions are clarificatory (re-explanation of what was said), surface (within the immediate topic, no extension), or exploratory (probing mechanism, implication, edge case, or opening new territory)

{rubric}
```

### L2: Productive Struggle and Reflection

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | None | Student seeks or accepts answers immediately; no evidence of effortful processing. |
| 2 | Minimal | Brief pause or hedged response, but does not pursue difficulty. |
| 3 | Slight | Acknowledges difficulty or uncertainty once without exploring it further. |
| 4 | Moderate | Visibly works through a problem; makes at least one revision or self-correction. |
| 5 | Clear | Persists through difficulty, reconsiders, and shows active self-monitoring. |
| 6 | Strong | Explicitly reflects on own thinking, revises positions, or asks questions about their own understanding. |
| 7 | Exceptional | Sophisticated self-regulation: notices confusion, re-frames the problem, and consolidates understanding within the conversation. |

Table 6: 
Rubric for L_{2}.

Prompt L_{2}

```text
Whether the student grapples with difficult ideas, tolerates uncertainty, revises their thinking, or reflects on their own understanding as opposed to seeking quick answers.

{rubric}
```

### L3: Student Curiosity

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | None | No observable curiosity signals; interaction is purely transactional. |
| 2 | Weak | One very minor signal of interest; could plausibly be politeness. |
| 3 | Occasional | Few mild signals of genuine interest but not sustained. |
| 4 | Moderate | Several clear signals of interest distributed across the conversation. |
| 5 | Notable | Interest is evident and consistent; student seems genuinely pulled toward the content. |
| 6 | Strong | Multiple strong signals; student is visibly trying to find out more. |
| 7 | Exceptional | Student’s interest is self-sustaining; they are in a clear state of inquiry rather than instruction-following. |

Table 7: 
Rubric for L_{3}.

Prompt L_{3}

```text
Observable signals that the student has a genuine drive to know more beyond polite participation. Look for: unprompted “but why” questions, expressed surprise or disbelief, unsolicited topic extensions, cross-domain connections, lingering on an interesting point.

{rubric}
```

### L4: Substantive Engagement and Agency

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | Absent | Substantive turns are rare relative to fillers; among them, virtually all are reactive and show no content interest beyond compliance. |
| 2 | Minimal | Only a small share of turns are substantive; elaboration is consistently thin; no proactive moves; engagement reads as social compliance. |
| 3 | Partial | A minority of substantive turns show elaboration; proactive moves are rare exceptions; flickers of content interest appear but are inconsistent. |
| 4 | Moderate | A meaningful share of substantive turns are elaborated and content-engaged; the student begins to share in shaping direction, with proactive moves appearing alongside reactive ones. |
| 5 | Clear | Most substantive turns are elaborated and reflect genuine content interest; the student steers about as often as they react; the tutor regularly follows student-initiated threads. |
| 6 | Strong | The large majority of substantive turns add depth, build cumulatively on prior exchanges, and reflect sustained interest; the student owns most directional choices and the tutor primarily supports their agenda. |
| 7 | Exceptional | Across substantive turns, the student consistently contributes depth, drives the conversational agenda, and is visibly immersed; the trajectory is unambiguously student-led and intellectually generative. |

Table 8: 
Rubric for L_{4}.

Prompt L_{4}

```text
The degree to which the student is a substantive, self-directing, content-interested participant combining depth of contribution, proactive shaping of the conversation, and genuine engagement with the material (as opposed to passive or compliant participation).

Three signals to weigh together (relative to the student’s total substantive turns):

Substance: share of substantive turns that include elaboration, connection-making, or building on prior exchanges, vs. one-sentence surface replies.
Agency: share of student moves that are proactive (introducing sub-topics, redirecting, challenging, extending) vs. purely reactive to a tutor prompt.
Content engagement: share of substantive turns showing genuine interest (personal connections, expressed reactions, voluntary returns to a topic) vs. mere compliance.

{rubric}
```

### T1: Instructional Quality

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | Poor | Explanations are unclear, inaccurate, or poorly scaffolded; likely to confuse the student. |
| 2 | Weak | Technically correct but flat, formulaic, or poorly sequenced. |
| 3 | Adequate | Clear and mostly appropriate; limited use of examples or scaffolding strategies. |
| 4 | Good | Clear explanations with appropriate examples; scaffolding present if not sophisticated. |
| 5 | Strong | Varied pedagogical strategies effectively used; well-paced and well-structured. |
| 6 | Very strong | High instructional sophistication, anticipates confusion, uses analogy and contrast, builds cumulatively. |
| 7 | Exemplary | Masterful instruction; every move serves a clear pedagogical purpose and the overall arc is coherent. |

Table 9: 
Rubric for T_{1}.

Prompt T_{1}

```text
Overall effectiveness of the tutor’s pedagogical approach clarity, accuracy, scaffolding, and appropriate use of explanations, examples, and feedback.

{rubric}
```

### T2: Depth and Metacognitive Probing

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | Surface only | Stays entirely at factual/recall level; never invites deeper thinking. |
| 2 | Minimal | Occasionally asks a “why” question but does not follow through. |
| 3 | Partial | Few attempts to prompt deeper thinking but exchanges remain shallow. |
| 4 | Moderate | Regularly asks students to explain reasoning or consider implications. |
| 5 | Consistent | Systematically probes for understanding and reflection across multiple exchanges. |
| 6 | Strong | Explicitly asks students to evaluate their own thinking, identify gaps, or compare approaches. |
| 7 | Exceptional | Sustained reflective dialogue; student and tutor examine together how understanding is being built. |

Table 10: 
Rubric for T_{2}.

Prompt T_{2}

```text
Whether the tutor pushes beyond surface content asking students to explain their reasoning, reflect on their understanding, consider alternatives, or identify the limits of what they know.

{rubric}
```

### T3: Cognitive Load Management

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | Severely mismanaged | Consistently overloads or trivialises; far too dense or far too sparse. |
| 2 | Poorly managed | Little awareness of load; frequently too long, too abstract, or too fragmented. |
| 3 | Inconsistent | Some responses well-pitched; others noticeably over- or under-loaded. |
| 4 | Adequate | Generally acceptable; few instances of clear overload or under-stimulation. |
| 5 | Good | Actively chunks information, checks for understanding, adjusts density across turns. |
| 6 | Strong | Clear intentionality in pacing sequences ideas, uses bridging summaries, allows processing time. |
| 7 | Expert | Masterful load management; challenge level continuously optimised to maintain productive engagement. |

Table 11: 
Rubric for T_{3}.

Prompt T_{3}

```text
Whether the tutor calibrates information density, pacing, and complexity to avoid overwhelming or under-challenging the student.

{rubric}
```

### T4: Adaptation to the Learner

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | No adaptation | Delivers a fixed script regardless of student responses. |
| 2 | Minimal | One superficial acknowledgment of the student; no change in approach. |
| 3 | Partial | Adapts in at least one instance (e.g., re-explains after confusion) but limited. |
| 4 | Moderate | Several adaptive moves adjusting vocabulary, depth, or topic based on student signals. |
| 5 | Clear | Consistently tracks the student’s level and interests; adaptation is regular and visible. |
| 6 | Strong | Personalises instruction meaningfully; references student’s prior statements, builds on student’s own framing. |
| 7 | Exceptional | Sophisticated learner modelling; instruction dynamically shaped by an accurate, ongoing read of the student. |

Table 12: 
Rubric for T_{4}.

Prompt T_{4}

```text
Whether the tutor adjusts language, framing, depth, and strategy in response to signals about the student’s understanding, interests, and needs as revealed within the conversation.

{rubric}
```

### T5: Curiosity Stimulation

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | None | Purely expository; no interest-stimulating strategies observed. |
| 2 | Incidental | One instance of an interesting framing or fact with no follow-through. |
| 3 | Occasional | Few moments that invite further thinking but not sustained. |
| 4 | Moderate | Interest-stimulating strategies used in several turns; student shows some observable response. |
| 5 | Consistent | Regularly introduces surprising, complex, or contradictory content; sustained sense of discovery. |
| 6 | Strong | Strategically sequences these strategies; the conversation has a feeling of unfolding discovery. |
| 7 | Masterful | Multiple strategies deployed with precision; the student’s interest becomes self-sustaining. |

Table 13: 
Rubric for T_{5}.

Prompt T_{5}

```text
Whether the tutor actively uses strategies to trigger and sustain the student’s interest and drive to explore. Look for: surprising facts, counterintuitive framings, revealing hidden complexity, surfacing contradictions, posing unresolved questions, leaving productive conceptual gaps rather than closing every question down.

{rubric}
```

### T6: Engagement Facilitation

| Score | Descriptor | Behavioral Anchor |
| --- | --- | --- |
| 1 | Monologue | Delivers uninterrupted information blocks; asks no questions, creates no participation space. |
| 2 | Token questions | Asks occasional yes/no or rhetorical questions that do not invite genuine thinking. |
| 3 | Some openings | A few participation opportunities but most turns are still tutor-dominated. |
| 4 | Moderate facilitation | Regularly asks questions and builds on student answers; genuine back-and-forth. |
| 5 | Active facilitation | Consistently creates engagement opportunities; guides toward answers rather than providing them. |
| 6 | Strong facilitation | Collaborative exchange; student and tutor contributions roughly balanced. |
| 7 | Exceptional | Master facilitator - every question purposeful, student thinking scaffolded, ownership consistently returned to the student. |

Table 14: 
Rubric for T_{6}.

Prompt T_{6}

```text
Whether the tutor creates genuine participation opportunities through questions, guiding without telling, and building on student contributions rather than delivering monologues.

{rubric}
```
