# Plato to Pareto Repository Guide

This repository contains the code and data analysis for the paper "Plato to Pareto". This README provides a guide to navigating the repository by mapping the methods described in the paper (Sections 2-7) to the corresponding files and directories.

## Overview of Methods Mapping

### 1. Estimating Immune Response
The estimation of immune response, quantified using RBC count and parasitemia (bystander killing), involves processing raw experimental data.
*   **Relevant Files:**
    *   `fig1/fig1.ipynb`: Loads raw data (`data_raw/DO_data.csv`) and processes it, likely calculating initial immune response metrics.
    *   `fig4/fig4.ipynb`: Analyzes processed immune intensity data.

### 2. Extraction of Maximal Values
This step involves extracting the maximal values for parasitemia, damage (RBC count, weight, and temperature changes), and immune response from the time-series data.
*   **Relevant Files:**
    *   `data/df_maxs.csv`: Contains the extracted maximal values for each mouse/strain.
    *   `fig1/fig1.ipynb`: Performs averaging and concatenation of data, likely part of the pipeline to extract these maximums.
    *   `fig4/fig4.ipynb`: Reads and uses `df_max_parents_other_infections.csv` to analyze maximal values across different infection types.

### 3. Normalization and Comparison Across Mice
Maximal values are standardized using z-scores to allow for comparison between different metrics and mice.
*   **Relevant Files:**
    *   `fig2/fig2.ipynb`: Loads and uses pre-calculated z-scored dataframes (`data/df_immune.csv`, `data/df_microbial.csv`, `data/df_rbc.csv`).
    *   `fig4/fig4.ipynb`: Contains analysis that likely involves or relies on this normalization step for comparing different infections.

### 4. Model Description
The paper describes a 3D ODE system for pathogen load, immune response, and damage, solved numerically.
*   **Relevant Context:** While explicit ODE simulation loops were not centrally located in the primary figure notebooks, the parameters defining this model are heavily analyzed in **Method 5**.

### 5. Parameter Sampling and Simulations
Parameters for the model (such as growth rates, repair rates, and immune efficiency) are sampled from distributions derived from experimental data.
*   **Relevant Files:**
    *   `SI_figures/parameters_distribution/data_parameter_analysis.ipynb`: Calculates and visualizes the distributions of key model parameters (e.g., parasite growth rate, weight loss repair rate, temperature loss repair rate) from the raw and processed data. This directly supports the parameter sampling methodology.

### 6. Archetype Analysis Using PCHA
The Principal Convex Hull Approximation (PCHA) algorithm is used to identify archetypes in the data.
*   **Relevant Files:**
    *   `fig2/fig2.ipynb`: The primary notebook for this analysis. It imports `py_pcha`, defines functions for sorting archetypes (`sort_archetypes`), and applies PCHA to the z-scored data (`MDI_mic`, `MDI_imm`, `MDI_rbc`).
    *   `SI_figures/statistical_calculations/archetype_number.ipynb`: Performs statistical calculations to validate the choice of the number of archetypes, plotting variance explained versus number of archetypes.
    *   `fig1/fig1.ipynb`: Also utilizes `py_pcha`, likely for preliminary analysis or consistent visualization across figures.

## Requirements

To run the code in this repository, you will need the following Python packages:

*   **numpy**
*   **pandas**
*   **matplotlib**
*   **scipy**
*   **scikit-learn**
*   **adjustText**
*   **py_pcha**

**Note:** The repository includes a local package named `DynamicModel_Package`. It is located in the root directory and is required for running the simulations (e.g., in `fig2/data/simulate_model.ipynb`).
