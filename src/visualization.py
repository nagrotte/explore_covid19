# src/visualization.py
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(data):
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True)
    plt.show()

def plot_pairplot(data):
    sns.pairplot(data)
    plt.show()
