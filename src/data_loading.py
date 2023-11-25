# src/data_loading.py
import pandas as pd

def load_dataset(file_path):
    # Load the dataset
    dataset = pd.read_csv(file_path)

    # Identify non-numeric columns
    non_numeric_cols = dataset.select_dtypes(exclude=['float64', 'int64']).columns

    # Convert non-numeric columns to numeric (replace non-convertible values with NaN)
    for col in non_numeric_cols:
        dataset[col] = pd.to_numeric(dataset[col], errors='coerce')

    return dataset  # Return the modified dataset
