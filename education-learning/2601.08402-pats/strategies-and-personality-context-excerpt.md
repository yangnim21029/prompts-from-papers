# Personality measurement and teaching-strategy context

Paper: PATS: Personality-Aware Teaching Strategies with Large Language Model Tutors

Authors: Rooein, Donya; Chowdhury, Sankalan Pal; Eremeeva, Mariia; Qin, Yuan; Nozza, Debora; Sachan, Mrinmaya; Hovy, Dirk

Source: https://arxiv.org/html/2601.08402v1#A2

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Published context sections B, D and Section 3; includes the taxonomy used to populate strategy placeholders.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix B Personality Test

Here we report the results of the personality traits in Table 4. In addition, we report the percentage of low  high for each trait in Figure 5.

|  |  | Image | Story |  |  |
| --- | --- | --- | --- | --- | --- |
| Model | Personality | F1 Score | Ave. F1 | F1 Score | Ave. F1 |
|  | Openness | 79.29% |  | 83.15% |  |
|  | Conscientiousness | 68.25% |  | 73.02% |  |
|  | Extraversion | 85.03% | 71.18% | 83.03% | 74.90% |
|  | Agreeableness | 70.43% |  | 71.33% |  |
| GPT | Neuroticism | 52.91% |  | 63.95% |  |
|  | Openness | 77.03% |  | 69.44% |  |
|  | Conscientiousness | 51.36% |  | 57.99% |  |
|  | Extraversion | 75.00% | 74.86% | 93.02% | 78.26% |
|  | Agreeableness | 93.02% |  | 90.06% |  |
| Gemini | Neuroticism | 77.89% |  | 80.76% |  |

Table 3: Performance of GPT and Gemini for Student Model backend. Numbers in bold indicate the best performance for each personality trait across the models. Overall, the Gemini model has a better average F1 score across all personality traits.

Figure 5: Percentage distribution of “Low” vs “High” personality traits among 110 students. We consider scores of \geq 3 as High, and \leq 3 as Low in traits.

| O | C | E | A | N | Popularity |
| --- | --- | --- | --- | --- | --- |
| H | H | L | H | H | 12.6% |
| H | H | H | H | H | 10.5% |
| H | H | H | H | L | 8.2% |
| L | H | L | H | H | 5.5% |
| H | L | H | H | H | 5.1% |
| L | H | H | H | H | 4.4% |
| H | L | L | H | H | 4.4% |
| L | L | L | H | H | 4.1% |
| H | L | L | H | L | 4.1% |
| H | H | L | H | L | 3.9% |
| L | L | H | H | L | 3.6% |
| L | H | L | H | L | 3.6% |
| H | L | H | H | L | 3.2% |
| H | H | H | L | L | 3.0% |
| H | H | L | H | L | 3.0% |
| L | L | L | L | H | 2.3% |
| H | H | L | L | H | 2.3% |
| L | L | H | H | L | 2.0% |
| L | L | H | H | H | 1.9% |
| L | H | H | L | H | 1.9% |
| L | H | H | L | L | 1.6% |
| H | H | H | L | H | 1.4% |
| L | L | H | L | L | 1.4% |
| H | H | L | L | H | 1.2% |
| L | H | L | L | H | 1.2% |
| L | L | L | L | L | 0.9% |
| L | H | H | L | L | 0.7% |
| L | L | H | L | H | 0.7% |
| H | L | L | L | H | 0.5% |
| H | L | L | L | L | 0.5% |
| L | L | L | H | L | 0.5% |
| H | L | H | L | L | 0.0% |

Table 4: Prevalence of student personality profiles based on the OCEAN model. Traits are coded as High (H) or Low (L). Students judged as borderline on a trait were split 50-50 into high (H) and low (L) groups. The top 10 personalities we used for our Human Experiments are highlighted in green.


## Appendix D Teaching Strategies

In Table 6, we describe our teaching strategies in the taxonomy together with references. The list of abbreviated strategies is available in Table 5.

| Teaching Strategy | Description | References | Example |
| --- | --- | --- | --- |
| 1. Choice-Based Dialog | Allow students to select from predefined responses to guide conversations, reducing cognitive load and anxiety. | Sweller (1988) | “You want to borrow a pen. Please choose the most polite request.” |
| 2. Collaborative Peer Teaching | Assign students to teach peers, increasing sense of responsibility and reducing overconfidence. | Agler et al. (2020) | “Imagine you are the teacher now, can you explain this concept to me?” |
| 3. Efficient Communication | Use minimal small talk to maintain focus and efficiency in instruction | Komarraju et al. (2009) | “Let’s start the key steps right away.” |
| 4. Friendly Tone | Use a friendly tone in the dialog. | McCrae and Costa (1999) | “Great effort! Let’s keep going together!” |
| 5. Gamified Learning Items | Use game elements like points, challenges, and rewards to enhance student engagement and motivation | Hamari et al. (2014) | “So far, you earned 60 points! Ready for the next challenge?” |
| 6. Meta-cognitive Prompt | Thinking techniques that involve awareness and regulation of one’s thought processes. | Komarraju et al. (2009) | “Can you explain how did you decide on this answer?” |
| 7. Motivational Encouragement | Send explanatory positive feedback to boost students’ confidence. | Mitrovic et al. (2013) | “Nice! ‘Walked’ is the correct past tense—good use of -ed.” |
| 8. Normalize Errors | Reinforce that errors are a natural part of learning, and create a safe space where students feel comfortable for their mistakes. | Bell and Kozlowski (2008) | “It’s okay to get it wrong—mistakes help us learn!” |
| 9. Playful Role-Play | Use role-play scenarios to simulate real-life situations and boost engagement. | Retny et al. (2017) | “Excuse me, could you tell me how to get to the train station?"(Student practices asking for directions in a travel scenario.) |
| 10. Progress Tracking | Help students monitor their progress to stay motivated. | Zimmerman and Kitsantas (2014) | “You’ve completed 3 out of 5 tasks, almost there!” |
| 11. Real-World Relevance | Link tasks to real-world problems and scenarios. | Busato et al. (1998) | “Where’s the pharmacy?" (Real-world question using location vocabulary.) |
| 12. Frequent Low-Stakes Quizzing | Integrate short quizzes throughout the session to reset attention and reinforce memory | Szpunar et al. (2013) | “Quick check: What’s 3 × 4?” |
| 13. Simulated Social Scenarios | Controlled, interactive tasks that mimic real-life social interactions for safe practice. | Agler et al. (2020) | “Imagine you’re working with Alex. He interrupts your idea. How to respond to him?” |
| 14. Solo First Then Support | Encourage independent work before providing help to build confidence and self-reliance | Firat (2022) | ‘The learner first attempts to match new words with definitions independently, and only after repeated mismatches does the ITS offer picture clues or example sentences.’ |
| 15. Step-by-Step Scaffolding | Offer structured, clearly instructed tasks to reduce cognitive load and confusion. | Komarraju and Karau (2005); Busato et al. (1998); Chandler and Sweller (1991) | “Step 1: Find the cat in the picture, Step 2: What color is it?” |
| 16. Structured Direct Instruction | Provide clear, explicit instruction to guide learning, especially for complex topics. | Agler et al. (2020); Busato et al. (1998) | “In one sentence, describe the tree in the picture” |
| 17. Task Variety | Provide diverse tasks in terms of topics, formats, or difficulty to cater to different interests. | Komarraju et al. (2009) | “You answered all the easy questions, now we study more complex items.” |

Table 6: Overview of the teaching strategy taxonomies, their descriptions, corresponding references, and examples.


| Trait | Level | Learner Characteristics | Teaching Strategies |
| --- | --- | --- | --- |
| Openness | High | Creative , Open-minded, Curious | Real-World Relevance; Task Variety |
|  | Low | Uncreative, Inflexible, Uninterested in learning | Structured Direct Instruction; Step-by-Step Scaffolding |
| Conscientiousness | High | Organized, Logical thinker, Positive attitudes, Strategic learner | Progress Tracking; Motivational Encouragement; Metacognitive Prompts |
|  | Low | Disorganised, Disengaged, Easily distracted | Step-by-step scaffolding; Gamified learning items; Frequent Low-Stakes Quizzing |
| Extraversion | High | Communicative, Talkative | Friendly Tone; Playful Role-Play |
|  | Low | Reluctant, Hesitant, Inarticulate | Choice-Based Dialogs; Motivational Encouragement |
| Agreeableness | High | Creative, Open-minded, Curious, Engaged learner | Collaborative Peer Teaching |
|  | Low | Disinterested, Inconsiderate, Impolite, Uncooperative | Structured Direct Instruction; Choice-Based Dialogs; Efficient Communication; Simulated Social Scenario |
| Neuroticism | High | Anxious, Nervous, Emotionally unstable | Motivational Encouragement; Structured Direct Instruction; Normalize errors |
|  | Low | Emotionally stable, Positive-minded, Confident | Task Variety; Solo First Then Support |

Table 1: Taxonomy of OCEAN personality-aligned teaching strategies in conversational ITSs with LLMs. Definitions for recommended teaching strategies for each trait are provided in Table 6 at Appendix D.


## 3 Taxonomy for Personality-Aligned Teaching Strategies

Learning science has shown that personality traits correlate with education-related factors such as learning approaches and learning outcomes Jensen (2015).
Following Liu et al. (2024) and Agler et al. (2020), we use the BFT theoretical framework to model students’ personality in tutoring conversations.
Each trait in this personality framework is instantiated at two levels (low/high) and is associated with distinct behavioral attributes in learners.
We define a set of corresponding teaching strategies for each personality profile, grounded in research from the learning sciences (see Table 1). They are the basis for designing adaptive pedagogical responses in our LLM-powered ITSs.

By doing so, we also present the first comprehensive review of prior learning science literature that examines the relationship between student personality traits and effective teaching strategies Busato et al. (1998); Komarraju and Karau (2005); Massa and Mayer (2006); Danesh and Soolmaz (2010); Harrington and Loffredo (2010); Tlili et al. (2016); Agler et al. (2020); Zuo et al. (2024). We extract strategies that were originally designed for traditional classroom environments and included both individual and group-based interventions. Then, to ensure feasibility within LLM-powered ITSs, we filtered for the strategies that are implementable based on the following criteria: (a) they are suitable for one-on-one teacher-student interactions, (b) they can be implemented within educational tasks with LLMs, and (c) they are appropriate for the targeted educational level. Following these criteria, we excluded strategies that require the physical presence of other students, rely on group dynamics, or are heavily context-dependent (e.g., classroom management techniques or peer-mediated instruction in co-located settings).
The results of our taxonomy are summarized in Table 1, which maps teaching strategies to each learner’s personality trait.

In our taxonomy, students with High Openness traits are inherently curious and creative. The most effective teaching approach for them is to provide real-world examples, following the Real-World Relevance strategy. Through this strategy, these students contextualize learning within meaningful scenarios.
In addition, they benefit from the Task Variety (Variety) strategy because high-openness students are more likely to respond well to creative and varied learning methods Komarraju et al. (2009).
In contrast, the literature suggests that students with Low Openness prefer routine, structure, and familiarity, making Structured Direct Instruction (Instr.) and Step-by-Step Scaffolding (Scaff.) strategies more effective, which reduces discomfort and disengagement Busato et al. (1998).
Learners with High Conscientiousness are more likely to benefit from structured learning environments through Motivational (Motiv.) and progress-tracking (Progress) tasks that match their self-discipline and planning skills (Komarraju et al., 2009). For example, after completing a task, the tutor might ask questions such as “Can you explain how you decided on this answer?”.
Conversely, Komarraju and Karau (2005) shows that Low Conscientiousness learners often get distracted, requiring step-by-step supervision and breaking tasks into smaller subtasks. Additionally, incorporating short, low-stakes quizzes throughout the session as recommended by Szpunar et al. (2013) can help reset attention and enhance cognitive engagement.

Danesh and Soolmaz (2010) characterizes High Extraversion learners as individuals who have difficulty engaging with e-learning content independently, particularly in the absence of peers. Such learners are more responsive to a friendly tone than a mechanical one, and benefit from instructional strategies that incorporate role-play and empathetic prompts, such as “Imagine you’re helping a friend…”. Those with Low Extraversion, who may be reluctant, benefit from a calm, non-intrusive, Choice-Based Dialog (Choice) strategy, which reduces pressure while encouraging gradual verbal expression. High Agreeableness often curious, open-minded, and engaged responds well to the Collaborative Peer Teaching strategy, which promotes responsibility Agler et al. (2020). In contrast, Low Agreeableness learners may exhibit disinterest or uncooperative behavior, benefiting more from structure and autonomy within clear boundaries Komarraju et al. (2009).

Finally, learners with High Neuroticism, who are often emotionally unstable or anxious, benefit from emotionally supportive learning environments that reduce stress. Teachers can support these students by normalizing mistakes (e.g., “Mistakes help us grow. Want to try again?”), breaking tasks into small, manageable steps, avoiding strict time constraints, and offering flexible pacing with reassuring prompts Zuo et al. (2024). Those learners with Low Neuroticism may be more capable of handling independent learning without added emotional support. In such cases, it is beneficial for teachers to provide autonomy by allowing students to choose topics, task order, or challenge level Firat (2022); Tlili et al. (2016). For example, prompts such as “Pick your next topic” or “Explore this on your own first, I’ll step in if needed” can foster independence. While our taxonomy summarizes a set of teaching strategies grounded in the literature (Table 1), our framework is intentionally flexible: educators can adapt or extend these strategies to their unique classroom contexts and pedagogical goals.
