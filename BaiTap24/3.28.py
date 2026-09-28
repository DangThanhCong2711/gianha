# bai_3_28.py
import numpy as np

w_328 = np.array([-2, 1, 0])
x_328 = np.array([2, 3, 1])
y_328 = 1

wTx_328 = np.dot(w_328, x_328)
y_pred_328 = 1 if wTx_328 >= 0 else -1
misclassified_328 = (y_pred_328 != y_328)

print("=== BÀI 3.28: KIỂM TRA VÀ CẬP NHẬT PERCEPTRON ===")
print(f"1. w^T * x = {wTx_328}, Dự đoán: {y_pred_328}, Thực tế: {y_328}")
print(f"   Mẫu có bị phân lớp sai không? {'Có' if misclassified_328 else 'Không'}")

if misclassified_328:
    w_new = w_328 + y_328 * x_328
    print(f"2. Trọng số sau cập nhật w_new = {w_new}")
    new_wTx = np.dot(w_new, x_328)
    print(f"3. Giá trị mới của w^T * x sau cập nhật = {new_wTx}")