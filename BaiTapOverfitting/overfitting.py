import csv

# Đọc dữ liệu từ file CSV
X_train, Y_train = [], []
with open('dulieu.csv.txt', mode='r') as file:
    reader = csv.DictReader(file)
    for i, row in enumerate(reader):
        if i < 5: # Lấy 5 dòng đầu làm Train
            X_train.append(float(row['X']))
            Y_train.append(float(row['Y']))

# Thuật toán tính trọng số (Đa thức) bằng Pure Python
def tim_trong_so(X, Y, bac):
    A = [[sum(x**(i+j) for x in X) for j in range(bac + 1)] for i in range(bac + 1)]
    b = [sum((x**i) * y for x, y in zip(X, Y)) for i in range(bac + 1)]
    # Khử Gauss đơn giản
    n = len(A)
    M = [row[:] + [val] for row, val in zip(A, b)]
    for i in range(n):
        pivot = M[i][i]
        M[i] = [x / pivot for x in M[i]]
        for j in range(n):
            if i != j:
                factor = M[j][i]
                M[j] = [M[j][k] - factor * M[i][k] for k in range(n+1)]
    return [row[-1] for row in M]

trong_so_overfit = tim_trong_so(X_train, Y_train, bac=4)
print("== CHẠY OVERFITTING ==")
print("Đã ép mô hình học vẹt thành công với đa thức bậc 4.")
print(f"Trọng số tìm được: {[round(w, 2) for w in trong_so_overfit]}")