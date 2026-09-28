X_train, Y_train = [1, 2, 3], [2.1, 3.9, 6.2]
X_val, Y_val = [4, 5], [8.1, 10.3]  # Tập kiểm định để theo dõi

w, b = 0.0, 0.0
learning_rate = 0.01
sai_so_val_tot_nhat = float('inf')
so_vong_lap_khong_cai_thien = 0

print("== CHẠY EARLY STOPPING ==")
for epoch in range(500):
    # Cập nhật trọng số (Training)
    for i in range(len(X_train)):
        loi_train = (w * X_train[i] + b) - Y_train[i]
        w -= learning_rate * (2 / len(X_train)) * X_train[i] * loi_train
        b -= learning_rate * (2 / len(X_train)) * loi_train

    # Tính sai số trên tập Validation
    sai_so_val = sum(((w * x + b) - y) ** 2 for x, y in zip(X_val, Y_val)) / len(X_val)

    # Kỹ thuật Dừng sớm
    if sai_so_val < sai_so_val_tot_nhat:
        sai_so_val_tot_nhat = sai_so_val
        so_vong_lap_khong_cai_thien = 0
    else:
        so_vong_lap_khong_cai_thien += 1

    if so_vong_lap_khong_cai_thien > 5:
        print(f"DỪNG SỚM TẠI VÒNG LẶP {epoch}! Vì sai số Validation bắt đầu tăng (Dấu hiệu Overfitting).")
        break