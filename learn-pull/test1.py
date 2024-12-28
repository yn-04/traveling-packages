import numpy as np

def linear_combination(x, w, b):
    return np.dot(x, w) + b

def sigmoid(z):
    return np.exp(-z)

def gradient_descent(x, y, lr, iterations):
    w = 0
    x = 0
    for i in range(iterations):
        pass