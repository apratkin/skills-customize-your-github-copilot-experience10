"""
Statistics with Python - Starter Code
This starter code provides a framework for data analysis using pandas and numpy.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Load and explore data
def load_and_explore_data(filename):
    """
    Load a CSV file and display basic information about it.
    
    Args:
        filename (str): Path to the CSV file
    
    Returns:
        pd.DataFrame: The loaded dataset
    """
    # TODO: Load the CSV file using pandas
    df = pd.read_csv(filename)
    
    # TODO: Display basic information
    print("Dataset Shape:", df.shape)
    print("\nFirst few rows:")
    print(df.head())
    
    print("\nData types:")
    print(df.dtypes)
    
    print("\nBasic statistics:")
    print(df.describe())
    
    print("\nMissing values:")
    print(df.isnull().sum())
    
    return df


# Task 2: Perform statistical analysis
def analyze_statistics(df):
    """
    Calculate statistical measures and relationships in the data.
    
    Args:
        df (pd.DataFrame): The dataset to analyze
    """
    # TODO: Calculate correlations between numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    if len(numeric_df.columns) > 1:
        print("\nCorrelation Matrix:")
        print(numeric_df.corr())
    
    # TODO: Calculate statistics for each numeric column
    for column in numeric_df.columns:
        mean_val = df[column].mean()
        median_val = df[column].median()
        std_val = df[column].std()
        print(f"\n{column}:")
        print(f"  Mean: {mean_val:.2f}")
        print(f"  Median: {median_val:.2f}")
        print(f"  Standard Deviation: {std_val:.2f}")


# Task 3: Create visualizations
def create_visualizations(df):
    """
    Create various visualizations for the dataset.
    
    Args:
        df (pd.DataFrame): The dataset to visualize
    """
    # TODO: Create visualizations
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) > 0:
        # Example 1: Histogram
        plt.figure(figsize=(12, 4))
        
        plt.subplot(1, 3, 1)
        numeric_df.iloc[:, 0].hist(bins=20, edgecolor='black')
        plt.title(f'Histogram of {numeric_df.columns[0]}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        
        # Example 2: Box plot
        plt.subplot(1, 3, 2)
        numeric_df.boxplot()
        plt.title('Box Plot of Numeric Columns')
        plt.ylabel('Value')
        
        # Example 3: Scatter plot (if we have at least 2 numeric columns)
        if len(numeric_df.columns) >= 2:
            plt.subplot(1, 3, 3)
            plt.scatter(numeric_df.iloc[:, 0], numeric_df.iloc[:, 1], alpha=0.6)
            plt.title(f'{numeric_df.columns[0]} vs {numeric_df.columns[1]}')
            plt.xlabel(numeric_df.columns[0])
            plt.ylabel(numeric_df.columns[1])
        
        plt.tight_layout()
        plt.savefig('analysis_visualization.png', dpi=100)
        print("\nVisualization saved as 'analysis_visualization.png'")
        plt.show()


# Main execution
if __name__ == "__main__":
    # Replace 'data.csv' with your actual dataset filename
    filename = 'data.csv'
    
    # Load and explore the data
    df = load_and_explore_data(filename)
    
    # Perform statistical analysis
    analyze_statistics(df)
    
    # Create visualizations
    create_visualizations(df)
