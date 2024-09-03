from math import sin,pi
from random import randint
def solve_gauss(A, b):
    n = len(A)

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j

        # Перестановка строк, чтобы обеспечить ненулевой диагональный элемент
        if A[max_row][i] == 0:
            raise ValueError("Ошибкa деления на 0")

        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Приведение уравнений к треугольному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            b[j] -= factor * b[i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            raise ValueError("Ошибкa деления на 0")

        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= A[j][i] * x[i]

    return x


A = [[2/3., 1/6., 0,0,0],
     [1/6., 2/3., 1/6.,0,0],
     [0, 1/6., 2/3.,1/6.,0],
        [0, 0, 1/6.,2/3.,1/3.],
        [0, 0, 0,2/3.,2/3.]]

b = [0,0,0,0,0]
print("Матрица коэф. системы: ")
for i in range(len(A)):
    print(A[i])
for i in range(len(A)):
    for j in range(len(A)):
        b[i]+=A[i][j]

resh=[1,1,1,1,1]


print("Свободный стобец: ",b)

x = solve_gauss(A, b)
print("Начальное решение: ",resh)
print("Найденное решение:", x)

