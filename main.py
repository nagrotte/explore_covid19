# main.py

import sys
sys.path.append("D:\\AIML\\COVID-19\\explore_covid19")  # Replace with the actual path to your project

from src.data_loading import load_dataset
from src.data_analysis import *
from src.visualization import *
from src.neural_network import NeuralNetwork

def main():
    # Load dataset
    dataset = load_dataset('data/COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_Facility.csv')

    # Data analysis
    get_dataset_info(dataset)
    get_descriptive_stats(dataset)
    check_missing_values(dataset)
    # Add more analysis functions as needed...

    # Visualization
    plot_correlation_matrix(dataset)
    plot_pairplot(dataset)
    # Add more visualization functions as needed...

    # Define neural network layers
    input_size = len(dataset.columns)  # Example: Get the number of input features from the dataset
    output_size = 1  # Example: Set the output size
    model = NeuralNetwork(input_size, output_size)

if __name__ == "__main__":
    main()
