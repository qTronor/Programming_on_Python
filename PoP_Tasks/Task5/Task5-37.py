def f(y, x):
    ans = 0
    for i in range(len(y)):
        ans += (1 + y[len(y) - 1 - i] ** 3 + 42 * x[i] ** 2) ** 2
    return ans * 87


print(f([-0.3, 0.72, 0.67, 0.0, -0.05, -0.69, 0.64, -0.28],
        [-0.43, 0.77, -0.2, 0.68, -0.6, -0.07, 0.78, -0.93]))
print(f([0.34, -0.87, 0.73, -0.65, -0.64, 0.65, -0.78, -0.77],
        [0.56, -0.95, -0.73, 0.77, 0.57, -0.28, 0.95, -0.18]))
print(f([0.4, -0.27, 0.52, 0.44, 0.27, -0.44, 0.67, -0.83],
        [0.47, -0.65, 0.61, 0.11, 0.94, -0.29, 0.7, -0.58]))
print(f([-0.49, -0.38, -0.83, -0.92, 0.82, -0.36, -0.74, -0.64],
        [-0.36, -0.59, -0.52, -0.71, -0.97, 0.28, 0.45, -0.57]))
print(f([0.07, -0.56, 0.14, -0.42, 0.43, 0.53, 0.79, 0.88],
        [0.32, 0.38, -0.68, -0.7, 0.89, -0.01, 0.21, -0.03]))
