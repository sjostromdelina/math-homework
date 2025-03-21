import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

def load_and_process_data():
    # Load MNIST dataset
    mnist = datasets.fetch_mldata('MNIST original', data_home='/tmp')
    
    # Split the data into features (X) and labels (y)
    X, y = mnist.data, mnist.target
    
    # Normalize the data between 0 and 1
    X = X / np.max(X)
    
    return X, y

# Main code execution starts here
if __name__ == "__main__":
    X, y = load_and_process_data()
    print("X shape:", X.shape)
    print("y shape:", y.shape)
