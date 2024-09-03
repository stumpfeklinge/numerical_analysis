import numpy as np

def thomas_algorithm(a, b, c, d):
    n = len(d)
    c_ = np.zeros(n-1)
    d_ = np.zeros(n)
    x = np.zeros(n)

    c_[0] = c[0] / b[0]
    d_[0] = d[0] / b[0]

    for i in range(1, n-1):
        c_[i] = c[i] / (b[i] - a[i-1]*c_[i-1])

    for i in range(1, n):
        d_[i] = (d[i] - a[i-1]*d_[i-1]) / (b[i] - a[i-1]*c_[i-1])

    x[-1] = d_[-1]
    for i in range(n-2, -1, -1):
        x[i] = d_[i] - c_[i]*x[i+1]

    return x
'''
# Матрица A и вектор b из заданной системы уравнений
A = np.array([[0.6666666666666667, -0.16666666666666666, 0, 0, 0],
              [0.16666666666666666, 0.6666666666666666, 0.16666666666666666, 0, 0],
              [0, 0.16666666666666666, 0.6666666666666666, 0.16666666666666666, 0],
              [0, 0, 0.16666666666666666, 1.0, 0.3333333333333333],
              [0, 0, 0, 0.3333333333333333, 1.6666666666666665]])

a = np.diag(A, k=-1)
b = np.diag(A)
c = np.diag(A, k=1)
d = np.array([2, 12, 18, 39, 68]) # Вектор b

solution = thomas_algorithm(a, b, c, d)
print(solution)
'''