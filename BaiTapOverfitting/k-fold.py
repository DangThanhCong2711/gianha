danh_sach_du_lieu = [
    (1, 2.1), (2, 3.9), (3, 6.2),
    (4, 8.1), (5, 10.3), (6, 12.1)
]

K = 3
kich_thuoc_fold = len(danh_sach_du_lieu) // K

print("== CHẠY K-FOLD CROSS VALIDATION ==")
for i in range(K):
    # Tách 1 phần làm Test, các phần còn lại làm Train
    bat_dau_test = i * kich_thuoc_fold
    ket_thuc_test = bat_dau_test + kich_thuoc_fold

    tap_test = danh_sach_du_lieu[bat_dau_test:ket_thuc_test]
    tap_train = danh_sach_du_lieu[:bat_dau_test] + danh_sach_du_lieu[ket_thuc_test:]

    print(f"Lần lặp {i + 1}:")
    print(f"  - Học trên {len(tap_train)} dữ liệu: {tap_train}")
    print(f"  - Kiểm tra trên {len(tap_test)} dữ liệu: {tap_test}\n")