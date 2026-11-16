import langroid as lr
import langroid.language_models as lm


class Actor:
    def __init__(
        self,
        model="groq/llama-3.3-70b-versatile",
        context_length=16384,
        name="Actor",
        temperature=None,
        character_prompt: str = "",
        provider="groq",
        retain_history=True,
    ):
        llm_kwargs = dict(
            chat_model=model,
            chat_context_length=context_length,
            timeout=600,
        )
        if temperature is not None:
            llm_kwargs["temperature"] = float(temperature)

        # Configure LLM based on provider
        if provider == "ollama":
            # For Ollama, use OpenAIGPTConfig with ollama/ prefix
            if not model.startswith("ollama/"):
                model = f"ollama/{model}"
            llm_kwargs["chat_model"] = model
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)
        elif provider == "llama.cpp":
            # For llama.cpp, use OpenAIGPTConfig with llama.cpp/ prefix
            if not model.startswith("llama.cpp/"):
                model = f"llama.cpp/{model}"
            llm_kwargs["chat_model"] = model
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)
        else:
            # Default to Groq (or any OpenAI-compatible provider)
            llm_config = lm.OpenAIGPTConfig(**llm_kwargs)

        self.config = lr.ChatAgentConfig(
            llm=llm_config,
            name=name,
        )
        self.agent = lr.ChatAgent(self.config)
        self.character_prompt = character_prompt
        self.retain_history = retain_history
        self.character_prompt_set = False

    def respond(self, prompt: str, turns: int = 1) -> str:
        # Handle character prompt: only add on first call if retaining history
        if self.character_prompt:
            if not self.retain_history:
                # Always add character prompt if not retaining history
                prompt = f"{self.character_prompt}\n\n{prompt}"
            elif not self.character_prompt_set:
                # Add character prompt only on first call if retaining history
                prompt = f"{self.character_prompt}\n\n{prompt}"
                self.character_prompt_set = True
                
        # Clear history if not retaining
        if not self.retain_history:
            self.agent.clear_history()
            
        task = lr.Task(
            self.agent, name=f"{self.config.name}Task", interactive=False
        )
        return task.run(prompt, turns=turns)

    def build_refinement_prompt(
        self, previous_answer: str, critic_feedback: str
    ) -> str:
        """Build a prompt for refining an answer based on critic feedback.

        Args:
            previous_answer: The actor's previous attempt at solving
            critic_feedback: Textual feedback from the critic (filtered
                           to exclude scores, error flags, and grading
                           criteria)

        Returns:
            A refinement prompt asking the actor to revise their answer
        """
        if self.retain_history:
            # If retaining history, previous answer is already in conversation
            # Just provide the critic feedback and refinement instruction
            return (
                f"The critic feedback was:\n{critic_feedback}\n\n"
                "Revise your solution accordingly. "
                "Provide a clear final answer."
            )
        else:
            # If not retaining history, include previous answer for context
            return (
                f"You previously answered:\n"
                f"{previous_answer}\n\n"
                f"The critic feedback was:\n{critic_feedback}\n\n"
                "Revise the solution accordingly. "
                "Provide a clear final answer."
            )

    def build_initial_prompt(self, problem_statement: str) -> str:
        """Build the initial prompt for solving a physics problem.

        Args:
            problem_statement: The problem description (in LaTeX format)

        Returns:
            A prompt instructing the actor to solve the problem with
            publication-quality rigor
        """
        return (
            "Solve the given physics problem with publication-quality "
            "rigor. The problem is written in LaTeX; preserve all LaTeX "
            "formatting.\\n\\n"
            "If this follows Critic feedback, address every point and "
            "provide a revised solution.\\n\\n"
            "You are a rigorous mathematical physicist.\\n"
            "Your entire response must be written in LaTeX (not "
            "markdown).\\n\\n"
            "Requirements:\\n"
            "    - Use proper LaTeX math mode for all mathematics and "
            "Greek letters.\\n"
            "    - Use standard LaTeX environments (equation, align, "
            "itemize, enumerate).\\n"
            "    - Number key equations and distinguish =, \\\\Rightarrow, "
            "and \\\\Leftrightarrow.\\n"
            "    - Define all notation, state assumptions, justify every "
            "step, and check validity, limits, and dimensions.\\n"
            "    - For QFT/String Theory: state the action, define "
            "transformations, show intermediate steps, verify "
            "identities.\\n"
            "    - For multi-part problems: solve parts (a), (b), (c) "
            "consistently.\\n\\n"
            "Structure your response as:\\n"
            "    \\\\subsection{Problem Restatement}\\n"
            "    \\\\subsection{Solution}\\n"
            "    \\\\subsection{Verification}\\n"
            "    \\\\subsection{Summary}\\n\\n"
            "Mark any non-rigorous steps with \\\\textbf{[UNCERTAIN: "
            "reason]}.\\n"
            "When responding to a Critic, systematically address or "
            "rigorously rebut each point. Reply in mathematics, and insist on "
            "explicit mathematical expressions instead of text descriptions.\\n\\n"
            f"Problem: {problem_statement}"
        )
