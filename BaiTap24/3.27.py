# bai_3_27.py
import numpy as np

w_327 = np.array([1, 2, -10])
x_327 = np.array([3, 4, 1])
wTx_327 = np.dot(w_327, x_327)
y_pred_327 = 1 if wTx_327 >= 0 else -1
y_true_327 = -1

print("=== BÀI 3.27: TÍNH TOÁN PERCEPTRON CƠ BẢN ===")
print(f"1. w^T * x = {wTx_327}")
print(f"2. Nhãn dự đoán: {y_pred_327}")
print(f"3. Nhãn thực tế: {y_true_327} -> Bị phân lớp sai? {'Có' if y_pred_327 != y_true_327 else 'Không'}")