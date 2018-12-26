import numpy as np
from sklearn.datasets import make_blobs


class Perceptron:
    def __init__(self):
        self.weights = None
        self.bias = None

    def train(self, X, Y, learning_rate=0.05, iters=100):
        assert len(X.shape) == 2
        assert len(np.unique(Y)) == 2

        samples, features = X.shape

        augmented_x = np.hstack((X, np.ones(shape=(samples, 1))))
        augmented_weights = np.zeros(features + 1)

        for i in range(iters):
            prediction = np.heaviside(np.dot(augmented_x, augmented_weights), 1)
            weights_delta = learning_rate * np.dot(augmented_x.T, (Y-prediction))

            if np.sum(weights_delta) == 0:
                break

            augmented_weights += weights_delta

        self.weights = augmented_weights[:-1]
        self.bias = augmented_weights[-1]

        return self.weights, self.bias

    def predict(self):
        pass


x, y = make_blobs(n_samples=10, n_features=3, centers=2, random_state=89)

algo = Perceptron()
print(algo.train(x, y, iters=100))