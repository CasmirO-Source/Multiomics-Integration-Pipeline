# Multi-omics Integration Pipeline

A small pipeline that generates two biological datasets, cleans them, joins them on shared sample IDs and plots the result. I built it in April 2025, before starting my MSc, to get comfortable with the basic steps of combining data from different sources.

The two datasets are gene activity (transcriptomics) and small-molecule levels (metabolomics) for the same ten samples. The data is synthetic, generated with fixed random seeds so every run gives the same output. About 5% of values are deliberately blanked out to mimic the gaps you get in real lab data.

## What it does

1. **Generate** (`Generate_Data.py`): creates 100 genes and 20 metabolites across 10 samples and writes them to `data/` as CSVs.
2. **Load and clean** (`Analysis.py`): reads both files, keeps numeric columns only and drops any row with a missing value.
3. **Join**: finds the samples present in both datasets and stacks them into one table.
4. **Select**: picks the two features with the most variation across samples.
5. **Plot**: splits samples into high and low groups on the first feature and saves a scatter plot to `results/sample_groups.png`.

Running it end to end, cleaning keeps 57 of 100 genes and 13 of 20 metabolites, giving a combined table of 70 features across 10 samples.

## What I'd do differently

Dropping every row with a missing value is the simplest approach, but here it throws away 43% of the genes. With real data I'd fill gaps instead (for example with the median for that feature) or only drop features above a set threshold of missing values, and I'd log how many rows each step removes so the losses are visible.

## Running it

```bash
git clone https://github.com/CasmirO-Source/Multiomics-Integration-Pipeline.git
cd Multiomics-Integration-Pipeline
pip install -r requirements.txt
python Generate_Data.py
python Analysis.py
```

Needs Python 3 with NumPy, pandas and Matplotlib.

## What's in the repo

- `Generate_Data.py`: creates the synthetic datasets
- `Analysis.py`: cleans, joins, selects and plots
- `data/`: the generated CSVs
- `results/`: the output plot
