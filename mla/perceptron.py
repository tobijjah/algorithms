import numpy as np
from mla.observer import Signal


class Perceptron:
    """
    A class for a simple machine learning algorithm called perceptron invented
    by Frank Rosenblatt 1957. A multi-layer perceptron builds a simple neural
    network. The perceptron algorithm is a binary linear classifier. Goal is
    to find a hyperplane that can separate a linearly separable dataset.
    """
    def __init__(self):
        self.weights = None
        self.bias = None

        self.weights_update = Signal('weights_update')

    def train(self, X, Y, learning_rate=0.01, iters=100, error_threshold=0):
        assert len(X.shape) == 2
        assert len(np.unique(Y)) == 2

        samples, features = X.shape

        augmented_x = np.hstack((X, np.ones(shape=(samples, 1))))
        augmented_weights = np.zeros(features + 1)

        for i in range(iters):
            prediction = np.heaviside(np.dot(augmented_x, augmented_weights), 1).astype(np.uint8)
            error = Y-prediction

            weights_delta = learning_rate * np.dot(augmented_x.T, error)

            if np.sum(np.absolute(error)) == 0 or np.sum(np.absolute(error))/samples <= error_threshold:
                break

            augmented_weights += weights_delta
            # report augmented weights to some external observer
            self.weights_update.fire(augmented_weights)

        self.weights = augmented_weights[:-1]
        self.bias = augmented_weights[-1]

        return self.weights, self.bias

    def predict(self, X):
        return np.heaviside(np.dot(X, self.weights) + self.bias, 1).astype(np.uint8)
