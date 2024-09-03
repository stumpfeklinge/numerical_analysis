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

x=[1,2,3,4,5,6]
y=[-1/6,-13/11,-23/18,-25/27,-13/38,19/51]
#m =int(input("Введите степень числителя: "))
#k =int(input("Введите степень числителя: "))
m=3
k=2
if k+m+1!=len(x):
    print("Ты адун")
A=[]
B=[]

for i in range(0,m+k+1):
    B.append(0)
    B[i]=-(x[i]**m)
print("Столбец свободных коэф.:",B)

for i in range(0,m+k+1):
    A.append([])
    for j in range(0,m+k+1):
        A[i].append(0)

for i in range(0,m+k+1):
    g = 0
    for j in range(0,m+k+1):
        if j==0:
            A[i][j]=1
        if j>0 and j<=m-1:
            A[i][j]=x[i]**j
        if j>m-1:
            #print(g)
            A[i][j]=-y[i]*(x[i]**(g))
            g+=1
print("Матрица системы:")
for i in range(m+k+1):
    print(A[i])

X=solve_gauss(A,B)
print("Ф-ия, которую хотим интерполировать f=(7-4x-5x^2+x^3)/(3+2x+x^2)")
print("Решение: ", X)
print(f"F(x)= ({X[0]}+{X[1]}*x+{X[2]}*x^2+x^3)/({X[3]}+{X[4]}*x+{X[5]}*x^2)")
