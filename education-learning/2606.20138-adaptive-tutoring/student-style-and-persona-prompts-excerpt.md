# Student style analyst and unmotivated learner simulator

Paper: Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring

Authors: Chang, Po-Chin; Hogan, Nicholas; Plaat, Aske; van der Meer, Michiel T.

Source: https://arxiv.org/html/2606.20138v2#A7

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — All published Appendix G content; the source illustrates the unmotivated persona and dynamic constraints, not all three learner personas as separate complete templates.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

## Appendix G Student Simulator Persona Design

To model the dynamics of real-world tutoring, we designed a robust student simulator based on three core principles. First, to capture authentic adolescent communication patterns, we extract stylistic summaries from randomly sampled real-world chat logs and inject them into the synthetic student’s system prompt. Second, to prevent the router overfitting to a single user type, we created three distinct learner profiles: Motivated, Mediocre, and Unmotivated. Finally, to mimic the unpredictable behavior of real user and avoid the inherent verbosity of LLMs, we implement a stochastic “inner monologue” mechanism that continuously injects dynamic constraints into the simulated student’s reasoning process.

### G.1 Linguistic Style Analysis

To ensure behavioral realism in the simulation, a high-capacity LLM was utilized to extract stylistic features from authentic student dialogue samples (\mathcal{D}_{chat}) using the following prompt:

System Instruction: Style Analyst

```text
# ROLE
You are a linguistic analyst specializing in adolescent communication patterns.

# TASK
Analyze the writing style of these Dutch high school student replies:
[Sampled_Chat_Logs]

# OUTPUT REQUIREMENTS
Describe the tone, grammar proficiency level, typical sentence structures, and common linguistic errors in one concise paragraph. This summary will be used to condition a student simulator.
```

### G.2 Unmotivated Student Persona and Dynamic Constraints

This appendix explains the logic for the Unmotivated student profile. Our simulator applies a dynamic prompt injection (monologue) to enforce realistic brevity and off-topic behaviors, preventing the LLM’s natural tendency toward verbosity.

System Instruction: Unmotivated Student Persona

```text
# ROLE
You are a distracted and unmotivated Dutch high school student learning {topic_title} in {subject}.

# BEHAVIORAL TRAITS
- Low Patience: Frequently ignore questions or provide random answers.
- Linguistic Realism: Use Dutch-English code-switching and heavy slang.
- Style Summary: {style_summary}
```

Dynamic Constraint Injection (Latent Thoughts)

```text
To prevent verbosity, the system appends a random "inner monologue" hint to each teacher utterance before it reaches the student simulator.

Examples of injected hints (randomly sampled):
- [Think: you are confused; reply in one short line.]
- [Think: ignore the question and talk about something else.]
- [Think: you give a wrong answer. Reply in one short line.]
```
