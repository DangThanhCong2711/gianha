import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Tạo dữ liệu (theo mẫu hình ảnh)[cite: 1]
np.random.seed(2)

means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 50  # Tăng số lượng mẫu để đánh giá trực quan hơn

X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

X = np.concatenate((X0, X1), axis = 1)
y = np.concatenate((np.ones((1, N)), -1*np.ones((1, N))), axis = 1).flatten()

# Thêm bias (thêm 1 vào đầu mỗi điểm dữ liệu)[cite: 1]
X_bias = np.concatenate((np.ones((1, 2*N)), X), axis = 0).T

# 2. Định nghĩa lớp Perceptron
class PerceptronClassifier:
    def __init__(self, lr=0.1, max_iter=100):
        self.lr = lr
        self.max_iter = max_iter
        self.w = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        for _ in range(self.max_iter):
            misclassified = False
            for xi, target in zip(X, y):
                if np.dot(xi, self.w) * target <= 0:
                    self.w += self.lr * target * xi
                    misclassified = True
            if not misclassified:
                break

    def predict(self, X):
        return np.where(np.dot(X, self.w) >= 0, 1, -1)

# 3. Huấn luyện và dự báo
model = PerceptronClassifier(lr=0.1, max_iter=100)
model.fit(X_bias, y)
y_pred = model.predict(X_bias)

# 4. Tính toán các độ đo đánh giá
acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred)
rec = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

print(f"--- KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH PERCEPTRON ---")
print(f"Accuracy  : {acc:.4f}")
print(f"Precision : {prec:.4f}")
print(f"Recall    : {rec:.4f}")
print(f"F1-score  : {f1:.4f}")