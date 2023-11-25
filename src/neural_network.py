# src/neural_network.py
import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, 20)  # Example: Input size to hidden size (20 neurons)
        self.fc2 = nn.Linear(20, output_size)  # Hidden size to output size

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Apply activation to 1st layer
        x = torch.sigmoid(self.fc2(x))  # Apply activation to 2nd layer
        return x
