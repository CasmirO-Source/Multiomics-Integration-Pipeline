import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load transcriptomic and metabolomic datasets from disk
def load_data(gene_file, molecule_file):
    try:
        gene_df = pd.read_csv(gene_file, index_col=0)
        molecule_df = pd.read_csv(molecule_file, index_col=0)
        print(f"Loaded gene data with {gene_df.shape[0]} genes and {gene_df.shape[1]} samples")
        print(f"Loaded metabolite data with {molecule_df.shape[0]} metabolites and {molecule_df.shape[1]} samples")
        return gene_df, molecule_df
    except Exception as e:
        print(f"Error loading files: {e}")
        return None, None

# Remove rows with missing values and make sure it is numeric-only data
def clean_data(df):
    df = df.dropna()  # Simple strategy: drop rows with NaNs
    df = df.select_dtypes(include='number')
    print(f"Cleaned data: {df.shape[0]} rows × {df.shape[1]} columns")
    return df

# Combine transcriptomic and metabolomic features for shared samples
def combine_data(gene_df, molecule_df):
    shared_samples = gene_df.columns.intersection(molecule_df.columns)
    if len(shared_samples) == 0:
        print("No shared samples!")
        return None
    combined = pd.concat([gene_df[shared_samples], molecule_df[shared_samples]])
    print(f"Combined data: {combined.shape[0]} features (genes + metabolites) × {combined.shape[1]} samples")
    return combined

# Select top 2 most variable features for visualisation
def pick_top_features(df):
    variances = df.T.var()
    top_two = variances.nlargest(2).index
    return df.loc[top_two], top_two

# Group samples based on the median of the first selected features
def group_samples(feature_data):
    first_feature = feature_data.iloc[0]
    median = first_feature.median()
    groups = first_feature.apply(lambda x: 'High' if x > median else 'Low')
    return groups

# Create and save a 2D scatter plot of the samples
def make_plot(features, groups, save_folder='results'):
    os.makedirs(save_folder, exist_ok=True)
    plt.figure(figsize=(6, 4))
    
    for group in ['High', 'Low']:
        mask = groups == group
        plt.scatter(features.iloc[0][mask], features.iloc[1][mask], label=group, s=50)

    plt.xlabel(f'Feature 1 ({features.index[0]})')
    plt.ylabel(f'Feature 2 ({features.index[1]})')
    plt.title('Sample Groups by Top Features')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'{save_folder}/sample_groups.png')
    plt.close()
    print(f"Plot saved: {save_folder}/sample_groups.png")

# Execution of the full pipeline
def run():
    print("Starting analysis")
    
    gene_file = 'data/transcriptomics_data.csv'
    molecule_file = 'data/metabolomics_data.csv'
    gene_df, molecule_df = load_data(gene_file, molecule_file)
    
    if gene_df is None or molecule_df is None:
        print("Missing data so we're not running.")
        return
    
    gene_df = clean_data(gene_df)
    molecule_df = clean_data(molecule_df)
    
    combined_df = combine_data(gene_df, molecule_df)
    if combined_df is None:
        return

    top_features, feature_names = pick_top_features(combined_df)
    groups = group_samples(top_features)
    make_plot(top_features, groups)

    print("Analysis completeddd")

if __name__ == "__main__":
    run()


