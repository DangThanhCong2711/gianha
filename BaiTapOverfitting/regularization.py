# Khởi tạo dữ liệu đơn giản
X_train = [1, 2, 3, 4, 5]
Y_train = [2.1, 3.9, 6.2, 8.1, 10.3]

# y = w * x + b
w, b = 0.0, 0.0
learning_rate = 0.01
epochs = 100
lambda_penalty = 0.1  # HỆ SỐ ĐIỀU CHUẨN (Ridge Regularization)

print("== CHẠY REGULARIZATION (ĐIỀU CHUẨN) ==")
for epoch in range(epochs):
    w_gradient = 0
    b_gradient = 0
    N = len(X_train)

    for i in range(N):
        x, y = X_train[i], Y_train[i]
        du_bao = w * x + b
        loi = du_bao - y

        # Tính đạo hàm có cộng thêm hình phạt (penalty) cho w
        w_gradient += (2 / N) * x * loi + (2 * lambda_penalty * w)
        b_gradient += (2 / N) * loi

    w -= learning_rate * w_gradient
    b -= learning_rate * b_gradient

print(f"Sau khi điều chuẩn, trọng số bị kìm hãm ở mức an toàn: w = {w:.3f}, b = {b:.3f}")