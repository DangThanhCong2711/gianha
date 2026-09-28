# --- CÁC HÀM TOÁN HỌC CƠ BẢN ---
def tinh_du_bao(x, trong_so):
    return sum(w * (x**i) for i, w in enumerate(trong_so))

def tim_trong_so(X, Y, bac):
    A = [[sum(x**(i+j) for x in X) for j in range(bac + 1)] for i in range(bac + 1)]
    b = [sum((x**i) * y for x, y in zip(X, Y)) for i in range(bac + 1)]
    n = len(A)
    M = [row[:] + [val] for row, val in zip(A, b)]
    for i in range(n):
        # Tránh lỗi chia cho 0 bằng cách chọn dòng có giá trị lớn nhất
        pivot_row = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[pivot_row] = M[pivot_row], M[i]
        pivot = M[i][i]
        if pivot == 0: continue
        M[i] = [val / pivot for val in M[i]]
        for j in range(n):
            if i != j:
                M[j] = [M[j][k] - M[j][i] * M[i][k] for k in range(n+1)]
    return [row[-1] for row in M]

def tinh_sai_so(X, Y, trong_so):
    return sum((y - tinh_du_bao(x, trong_so))**2 for x, y in zip(X, Y)) / len(X)

# --- CHẠY THỬ NGHIỆM MORE DATA ---
print("== MINH HỌA: THÊM DỮ LIỆU (MORE DATA) ĐỂ TRÁNH OVERFITTING ==")

# 1. Tập dữ liệu quá nhỏ (Chỉ 4 điểm)
X_nho, Y_nho = [1, 2, 3, 4], [2.1, 3.9, 6.2, 8.1]

# 2. Tập dữ liệu lớn hơn (Thêm 6 điểm mới)
X_lon = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
Y_lon = [2.1, 3.0, 3.9, 5.0, 6.2, 7.1, 8.1, 9.2, 10.3, 11.1]

# 3. Tập Test chung (Dữ liệu chưa từng thấy)
X_test, Y_test = [1.2, 2.8, 4.8], [2.5, 5.8, 9.8]

# Ép dùng chung đa thức phức tạp (Bậc 3)
bac_da_thuc = 3

trong_so_nho = tim_trong_so(X_nho, Y_nho, bac_da_thuc)
print("\n1. KHI CÓ ÍT DỮ LIỆU (4 điểm):")
print(f"  - Sai số Train: {tinh_sai_so(X_nho, Y_nho, trong_so_nho):.6f} (Khớp hoàn hảo 100%)")
print(f"  - Sai số Test:  {tinh_sai_so(X_test, Y_test, trong_so_nho):.6f} (Lỗi cao do học vẹt)")

trong_so_lon = tim_trong_so(X_lon, Y_lon, bac_da_thuc)
print("\n2. KHI CÓ NHIỀU DỮ LIỆU (10 điểm):")
print(f"  - Sai số Train: {tinh_sai_so(X_lon, Y_lon, trong_so_lon):.6f} (Không còn học vẹt được)")
print(f"  - Sai số Test:  {tinh_sai_so(X_test, Y_test, trong_so_lon):.6f} (Giảm đáng kể so với trước)")