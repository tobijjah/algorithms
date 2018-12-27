import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs

from mla.perceptron import Perceptron


def wrapper(axes, x1, x2):
    def draw_line(*args):
        augmented_weights = args[0]
        xs = np.linspace(x1-1, x2+1, 2)
        ys = -(augmented_weights[0] * xs)/augmented_weights[1] - augmented_weights[2]/augmented_weights[1]
        axes.plot(xs, ys, alpha=0.2, color='gray')

    return draw_line


if __name__ == '__main__':
    perceptron = Perceptron()
    fig, axes = plt.subplots()

    X, Y = make_blobs(n_samples=100, n_features=2, centers=2)
    x_min = np.amin(X, axis=0)[0]
    x_max = np.amax(X, axis=0)[0]

    draw = wrapper(axes, x_min, x_max)
    perceptron.weights_update.connect(draw)

    weights, bias = perceptron.train(X, Y, iters=1000)

    xs = np.linspace(x_min-1, x_max+1, 2)
    ys = -(weights[0]*xs)/weights[1] - bias/weights[1]

    axes.scatter(X[:, 0], X[:, 1], c=Y, marker='.')
    axes.plot(xs, ys, color='lightgreen')

    plt.show()
