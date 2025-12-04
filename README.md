#  Multiomics Data Simulation and Analysis Pipeline

This was one of my favourite projects to complete. Although I only completed it utilising transcriptomics and metabolic data, the pipeline could be extended to include more data types to increase its complexity and difficulty. It was quite challenging yet rewarding for me to create and will aid me greatly in my preparation for postgraduate studies

This repository contains a pipeline for simulating, processing, and visualising multiomics datasets (transcriptomics and metabolomics). It is designed as part of a bioinformatics learning portfolio, demonstrating core concepts in data simulation, preprocessing, integration, and visualisation.

This project reflects my interest in biological data analysis and serves as preparation for postgraduate study in Bioinformatics.

---

## Project Goals

- Demonstrate understanding of multiomics data structures (genes + metabolites)
- Practice data cleaning and feature selection methods
- Apply simple statistical strategies to visualise sample-level variation
- Create reproducible, structured Python code suitable for academic or industry settings

---

##  Overview

The pipeline simulates synthetic omics data to mimic real-world conditions (including missing values), then processes and visualizes the data to identify patterns across samples.

It includes two main Python scripts:

1. 'generated_data.py' – simulates and exports fake transcriptomics and metabolomics datasets
2. 'analysis.py' – loads, cleans, combines, and visualizes the data using basic statistical methods

---

##  Project Structure
Multi_Omics_Pipeline/
├── data/ # Auto-generated CSV files (gene & metabolite data)
├── results/ # Output plot showing how samples group together based on the two most variable features selected from the combined data
├── git.ignore # Stores my temporary files created by my device
├── analysis.py # Analyse and visualise the data
├── generated_data.py # Generate synthetic omics data
├── requirements.txt # Package dependencies
└── README.md # Project documentation

---
## Usage Instructions

1. Clone the repository
git clone https://github.com/CasmirO-Source/Bioinformatics.git
cd Bioinformatics
2. Install dependencies
pip install -r requirements.txt
3. Generate the synthetic data
python scripts/generated_data.py
4. Run the analysis
python scripts/analysis.py

## Dependencies

numpy
pandas
matplotlib

Install them all at once using:

pip install -r requirements.txt


## Skills Demonstrated

Data simulation and handling biological noise
Missing value management
Sample intersection and omics integration
Feature variability analysis
Data visualization using Python

## Academic Relevance

This project was developed as a foundational exercise in multiomics data processing, which is a core skill in modern bioinformatics research. It reflects my interest in applying computational tools to real-world biological data and prepares me for my coursework and research in Bioinformatics.

**Developed**: April 2025 | **Uploaded**: May 2025
