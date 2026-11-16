# Empathy on Demand: How Empathic AI Can Scale Emotional Support for Online Harassment

This repository provides the **data, code, and analysis** for the project.

We share all materials to ensure transparency, reproducibility, and traceability of the findings. The repository contains:\
- Code for fetching LLM API responses and processing human and AI response data\
- Statistical analysis scripts and notebooks\
- All corresponding raw and processed datasets

------------------------------------------------------------------------

## Repository Structure

The structure follows the studies described in the paper:

-   **pre-test/**
-   **study1/** -- subdivided into:
    -   `human_experts/`
    -   `human_nonexperts/`
    -   `llm/`
    -   `studies_comparison/` (cross sample analyses)
-   **study2/**

Each study (and subsample) follows the same internal structure:\
- `analysis/` -- scripts and notebooks for data processing and statistical analyses\
- `data/` -- raw and processed datasets

------------------------------------------------------------------------

## Reproducing the Analyses

You can reproduce all analyses in two ways:

1.  **Re-generate LLM responses and open-text features** by running the respective scripts.\
    \> *Note: LLM outputs may vary slightly due to model stochasticity.*

2.  **Run all statistical analyses directly** using pre-processed data (no need to re-generate responses).

    -   Study 1: `01_betweenStudiesAnalysis.ipynb`
    -   Study 2: `02_analysis.ipynb`

------------------------------------------------------------------------

## Software and Dependencies

Analyses were conducted using **Python 3.12.6** and **R 4.3**.

### Python

1.  Create a Python 3.12.6 environment.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### R

All required R packages are loaded at the beginning of each script (install as needed).

------------------------------------------------------------------------

## Getting Started

After setting up your environment, simply open the analysis notebooks to reproduce our results or explore the data. We welcome feedback and encourage reuse of these materials in the spirit of open science.

------------------------------------------------------------------------

## License
- **Code**: Released under the [MIT License](./LICENSE).  
- **Data**: Released under the [CC BY 4.0 License](./DATA_LICENSE).  

If you use this repository, please cite our paper and acknowledge the source.
