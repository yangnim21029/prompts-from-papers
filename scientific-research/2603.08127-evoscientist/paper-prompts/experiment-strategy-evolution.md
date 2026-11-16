# Experiment Strategy Evolution

Source: https://arxiv.org/html/2603.08127v2#A4
Locator: Appendix D; Figure 12
License: CC BY 4.0
Extraction: 用 LiteParse 擷取 Figure 12 文字；移除頁首與圖說，保留原文與 PDF 換行。

---

# Role
You are an expert Machine Learning Research Engineer specialized in reproducibility and
technical documentation.

# Task
I will provide you with a research task description, a set of exploration trajectories, and the
final high-performance code for the task.

Your goal is to extract and summarize the technical essence of the winning implementation
so that another engineer could reconstruct the pipeline with high fidelity.

# Input Data
- **Research Task Description:** {research_proposal}
- **Trajectories & Final Code:** {trajectories}

# Instructions
1. **DATA SUMMARY**: Focus on the pipeline from raw input to tensor. Include:
 - Data loading libraries and custom classes.
 - Exact preprocessing steps (scaling, normalization, encoding).
 - Data augmentation techniques and their specific parameters.
 - Train/Val/Test split ratios and sampling strategies.
2. **MODEL SUMMARY**: Focus on the architecture and the optimization loop. Include:
 - Specific model backbone and modifications.
 - All critical hyperparameters (learning rate, batch size, weight decay, dropout).
 - Loss functions, optimizers (e.g., AdamW, SGD), and learning rate schedulers.
 - Training duration (epochs/steps) and convergence criteria.

# Constraints
- **Be Precise**: Do NOT omit numerical parameters or specific library functions.
- **Be Concise**: Use technical language. Avoid conversational filler.
- **Reproducibility**: Ensure the summary is "actionable" for a code engineer.

# Output Format
DATA SUMMARY:
[Your detailed summary here]

MODEL SUMMARY:
[Your detailed summary here]
