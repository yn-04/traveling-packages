import numpy as np

def linear_combination(x, w, b):
    return np.dot(x, w) + b

def sigmoid(z):
    return np.exp(-z)