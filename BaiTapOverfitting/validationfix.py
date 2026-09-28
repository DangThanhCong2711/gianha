# (Copy lại 3 hàm toán học: tinh_du_bao, tim_trong_so, tinh_sai_so từ file ở trên vào đây)
def tinh_du_bao(x, trong_so): return sum(w * (x ** i) for i, w in enumerate(trong_so))


def tinh_sai_so(X, Y, trong_so): return sum((y - tinh_du_bao(x, trong_so)) ** 2 for x, y in zip(X, Y)) / len(X)


def tim_trong_so(X, Y, bac):
    A = [[sum(x ** (i + j) for x in X) for j in range(bac + 1)] for i in range(bac + 1)]
    b = [sum((x ** i) * y for x, y in zip(X, Y)) for i in range(bac + 1)]
    n = len(A)
    M = [row[:] + [val] for row, val in zip(A, b)]
    for i in range(n):
        pivot_row = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[pivot_row] = M[pivot_row], M[i]
        pivot = M[i][i]
        if pivot == 0: continue
        M[i] = [val / pivot for val in M[i]]
        for j in range(n):
            if i != j: M[j] = [M[j][k] - M[j][i] * M[i][k] for k in range(n + 1)]
    return [row[-1] for row in M]


# --- CHẠY THỬ NGHIỆM VALIDATION ---
print("== MINH HỌA: DÙNG VALIDATION ĐỂ CHỌN MÔ HÌNH ==")

# Chia dữ liệu thành 3 tập riêng biệt
X_train, Y_train = [1, 2, 3, 4, 5], [1.9, 4.1, 6.0, 8.2, 9.8]  # Học
X_val, Y_val = [1.5, 3.5, 4.5], [3.0, 7.0, 9.1]  # Trọng tài chọn mô hình
X_test, Y_test = [2.5, 5.5], [5.1, 11.0]  # Đánh giá cuối cùng

bac_tot_nhat = 1
sai_so_val_nho_nhat = float('inf')

print("\nQuá trình thử nghiệm các độ phức tạp khác nhau:")
for bac in range(1, 5):  # Thử đa thức từ bậc 1 đến bậc 4
    trong_so = tim_trong_so(X_train, Y_train, bac)

    sai_so_train = tinh_sai_so(X_train, Y_train, trong_so)
    sai_so_val = tinh_sai_so(X_val, Y_val, trong_so)

    print(f" - Đa thức bậc {bac}: Lỗi Train = {sai_so_train:.4f} | Lỗi Validation = {sai_so_val:.4f}")

    # Kỹ thuật cốt lõi: Chỉ quan tâm mô hình nào có lỗi Validation nhỏ nhất!
    if sai_so_val < sai_so_val_nho_nhat:
        sai_so_val_nho_nhat = sai_so_val
        bac_tot_nhat = bac
        trong_so_tot_nhat = trong_so

print("\n=> KẾT LUẬN TỪ TRỌNG TÀI VALIDATION:")
print(f"Mô hình được chọn là Đa thức bậc {bac_tot_nhat}.")
print(f"(Lưu ý: Đa thức bậc 4 có lỗi Train thấp nhất nhưng bị loại vì Overfitting làm lỗi Val tăng cao).")

sai_so_test_cuoi_cung = tinh_sai_so(X_test, Y_test, trong_so_tot_nhat)
print(f"\n=> Lỗi trên tập Test cuối cùng (Dữ liệu thực tế): {sai_so_test_cuoi_cung:.4f}")