import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.1, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.w = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)

        for _ in range(self.max_iter):
            misclassified = False
            for xi, target in zip(X, y):
                linear_output = np.dot(xi, self.w)
                y_pred = 1 if linear_output >= 0 else -1

                if y_pred != target:
                    self.w += self.learning_rate * target * xi
                    misclassified = True

            if not misclassified:
                break

    def predict(self, X):
        linear_output = np.dot(X, self.w)
        return np.where(linear_output >= 0, 1, -1)