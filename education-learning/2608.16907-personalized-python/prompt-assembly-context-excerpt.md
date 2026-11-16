# Generation and tutor assembly context

Paper: Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning

Authors: Chung, Angel Tsai-Hsuan; Zhang, Botong; Kung, Ling-Chieh; Bastani, Hamsa; Bastani, Osbert

Source: https://arxiv.org/html/2608.16907v1#A1.SS2

License: https://creativecommons.org/licenses/by/4.0/

Status: EXCERPT — Published procedural context, not an additional complete prompt. Some Figure 11/12 text is repeated here as part of the original sections.

The source wording below is retained; HTML layout is converted to Markdown/text.

---

### A.2 RAG System for Problem Generation

We generate Python programming questions based on instructional materials using the RAG-based LLM pipeline shown in Fig. 10. For each generation request, we prompt the LLM with (i) the main instructional content, (ii) optional additional content (e.g., prior modules), and (iii) a list of existing questions to discourage duplicates. The model is instructed to output a JSON object containing two coding questions (in English with a traditional Chinese translation), along with a template solution stub, a working sample solution, and a comprehensive assert-based test suite. To encourage variety in the generated questions (e.g., different scenarios and wording), we use sampling settings that allow some randomness (temperature = 1.0, top-p= 0.7, top-k= 200).

The system prompt provides the educational content and high-level role instructions, while the user prompt specifies the required output format and constraints (difficulty levels, bilingual problem statements, and test-suite requirements); we show the system prompt in Figure 11 (we omit the user prompt due to its long length). We generate questions in batches of two.

Figure 10: Human-AI RAG pipeline for practice problem generation. Course materials and past exams are retrieved as reference contents for an LLM (ChatGPT) to generate programming questions, solutions, and test cases. Each generated output is validated using a Python script that checks functional correctness and consistency. When validation fails, a secondary LLM (Claude) iteratively revises the components until they pass. Teaching assistants then review finalized questions for clarity and quality before deployment.

```text
You are a knowledgeable AI assistant designed to help generate questions based on educational content.
Main content:
{MAIN_DOCUMENT_TEXT}

Additional content:
{ADDITIONAL_DOCUMENT_TEXT}

Your goal is to create well-structured, meaningful, and educational coding questions based on the content provided.
You may combine the concepts taught in the additional contents with the main content for generating unique and insightful questions.
You should always ensure the correctness of your output and follow the question generation format carefully.
When answering, adhere strictly to Python programming conventions and ensure the output format is clean and structured.
```

Figure 11: System prompt for RAG practice problem generation pipeline.


### A.3 GenAI Chatbot Tutor

##### Tutor integration and shared context.

Students interacted with our GenAI tutor (powered by OpenAI’s GPT-4o model) embedded in the learning platform during practice. The tutor was available in both the treatment (RL sequencing) and control (fixed sequencing) conditions, and the tutoring model and prompting pipeline were held constant across conditions.

At each practice step, the tutor received a user prompt formed by concatenating the student’s query with the current practice problem, relevant metadata (e.g., difficulty), and the sample solution code and/or answer key. The tutor was instructed in the system prompt (see Fig. 12) to keep responses brief and to explain concepts at a middle-school level. This design enabled the tutor to provide accurate, targeted hints while enforcing a strict “no direct answers” policy.

Base system prompt.

You are a Python tutor. Your goal is to help students develop a deeper understanding of Python while keeping them focused on learning. Keep responses brief, concise, and to the point---exercise restraint.

Explain to me like I’m a middle school student and make sure to use the solution code provided in the context.

Figure 12: Common base system instruction (used in all conditions)

##### Pedagogy randomization.

The focus of this paper is on RL-based sequencing of practice problem difficulty. However, we also randomized the AI tutor’s system prompt in this study (see our pre-registered plan in D.4).
All our pedagogy prompts shared the following instructions: (i) do not provide direct answers or full code; (ii) diagnose whether the student’s difficulty is problem formulation versus Python syntax/logic and respond accordingly; (iii) keep responses concise; (iv) maintain role consistency; and (v) respond in Traditional Chinese when the student writes in Chinese. They only differed in pedagogical emphasis. We find no meaningful or statistically significant differences across these pedagogy conditions in exam performance or engagement outcomes; accordingly, we do not focus on pedagogy comparisons in this paper. We show that our results are robust to this additional randomization in F.1.
