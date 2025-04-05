import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data():
    # Load data
    data = pd.read_csv('data.csv')
    x = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = load_and_prepare_data()
