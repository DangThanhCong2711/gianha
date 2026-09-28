# bai_3_26.py

def f(x):
    return x**2 - 4*x + 5

def grad_f(x):
    return 2*x - 4

x = 5.0
lr = 0.2

print("=== BÀI 3.26: GRADIENT DESCENT ===")
print(f"Bước 0: x = {x}, f(x) = {f(x)}, f'(x) = {grad_f(x)}")

for i in range(1, 5):
    grad = grad_f(x)
    x = x - lr * grad
    print(f"Bước {i}: x = {x:.4f}, f(x) = {f(x):.4f}, f'(x) = {grad:.4f}")