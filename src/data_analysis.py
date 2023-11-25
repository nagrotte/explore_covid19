# src/data_analysis.py
def get_dataset_info(data):
    return data.info()

def get_descriptive_stats(data):
    return data.describe()

def check_missing_values(data):
    return data.isnull().sum()
