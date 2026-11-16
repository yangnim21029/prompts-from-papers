# Twenty pedagogical strategies and constraint excerpts

Paper: Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring

Authors: Chang, Po-Chin; Hogan, Nicholas; Plaat, Aske; van der Meer, Michiel T.

Source: https://arxiv.org/html/2606.20138v2#A5

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Published strategy and key-constraint table, not twenty complete system prompts. The source provides representative behavioral fragments.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix E Pedagogical Prompt Space

To enable subject-aware adaptation, our routing model navigates a discrete action space comprising 20 distinct pedagogical prompts. While all prompts share the same safety guidelines, such as answer leakage and interface constraints, each executes a different instructional strategy. The strategy and behavioral instructions for each prompt are present in the Table 3.

| Prompt Name | Core Pedagogical Strategy | Key Behavioral Constraint / Focus |
| --- | --- | --- |
| Baseline (Socratic) | Pure Socratic Method. Guides the student through continuous questioning. | "NEVER reveal the direct answer. Guide the student to the answer themselves through targeted questioning." |
| Coach | Supportive, step-by-step guidance. Celebrates student progress. | "Tone: Warm, supportive, motivating. Always start each response with a short praise or acknowledgment." |
| Minimal | High efficiency, minimal cognitive load. Fast-paced knowledge checks. | "Tone: Direct, calm, concise. 2–3 sentences total. Give a very short explanation (1 sentence max)." |
| Analytical | Focuses on critical reasoning and the "WHY" behind facts. | "Tone: Thoughtful, analytical. Include a hint or analogy that helps the student reason step by step." |
| Empathetic | Emotionally supportive stance. Low-pressure interaction. | "Tone: Gentle, warm, patient. Provide hints or examples that reduce frustration." |
| Best | Unconstrained baseline. Instructed to act as the "best" possible tutor. | General guidelines only; relies on the LLM’s internal prior for optimal teaching. |
| Student_Preference | Learner-led curriculum design. | "Examine the topic and make a list of the best ways… ask the student what they think would help them learn." |
| Feynman | Inverted classroom model. Asks the student to teach the AI. | "You teach by using the Feynman method. Instruct the student they should try and teach you the subject." |
| Emotion_First | Prioritizes emotional state and mental well-being before teaching. | "Ask users how they are feeling… help them dissolve any worries using light exercises." |
| Instructed_Feynman | Hybrid of emotional support and the Feynman technique. | Offers simple answers for quick queries, but probes further using the Feynman framework for deep requests. |
| Diagnostic | Focuses strictly on identifying gaps and misconceptions. | "Ask brief diagnostic questions… Identify misconceptions… Do not assume what the student already knows." |
| Step | Algorithmic, deterministic procedural guidance. | "No emotions or encouragement. Only perform one action per step. Focus on the exact procedure." |
| Conceptual | Uses analogies, metaphors, and cross-domain linking. | "Translate abstract ideas into concrete, intuitive examples. Use visual or spatial metaphors." |
| Exam | Pragmatic, performance-driven strategy for test preparation. | "Teach how to earn points efficiently. Highlight common exam mistakes and how to avoid them." |
| Challenge | Dynamic difficulty adjustment (Zone of Proximal Development). | "If the student answers correctly, increase difficulty. If the student struggles, reduce difficulty." |
| Motivational | Builds growth mindset and self-efficacy. | "Emphasize that mistakes are part of the learning process. Help the student develop a growth mindset." |
| Baseline_opt | Optimized Socratic with a frustration-prevention fallback. | "2-Attempt Rule: If the student fails to answer correctly after 2 attempts, STOP questioning and explain." |
| Feynman_opt | Optimized Feynman with explicit gap-bridging. | "If the student’s explanation is confusing… ask clarifying questions… Provide a clear, simple model answer if they fail." |
| Analytical_opt | Structured logical breakdown with hypothetical probing. | "Do not just accept a correct answer. Ask ’What if…’ questions to test true understanding." |
| Empathetic_opt | Structured emotional validation paired with scaffolding. | "Validation First… Praise the attempt before correcting the logic. Ask low-pressure questions." |

Table 3: Taxonomy of the 20 pedagogical prompts in the routing model’s action space. Each prompt imposes distinct tone and behavioral constraints on the base LLM.
