
from scipy.integrate import quad
from gauss import solve_gauss
from math import cos,pi,sin
import matplotlib.pyplot as plt
import numpy as np

def cosi(x,i):
    return cos(x)*x**i

def sini(x,i):
    return sin(x)*x**i

# Функция для подынтегрального выражения x^i
def integrand(x, i,j):
    return x**(i+j)


a = float(input('Введите нижнюю границу диапазона: '))
b = float(input('Введите верхнюю границу диапазона: '))
n=int(input("Введите число n:\n"))

Grama_matr = [[0 for _ in range(n)] for _ in range(n)]
free_values = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        result, error = quad(integrand, a, b, args=(i,j))
        Grama_matr[i][j] = result


for i in range(n):
    #result, error = quad(sini, a, b, args=(i,))
    result, error = quad(cosi, a, b, args=(i,))
    free_values[i] = result

print("Матрица Грама:")
for i in range(n):
    print(Grama_matr[i], ' | ', free_values[i])


res = solve_gauss(Grama_matr, free_values)
print('Решение   = ', res)

tochka=float(input("Введите точку для подстановки:\n"))
s=0
for i in range(n):
   s+=(tochka**i)*res[i]

print(f"Значение функции в точке {tochka} = {s}")

x_values = np.array([i / 25 for i in range(-50,50)])
y_values = np.zeros(100)
y_cos = np.zeros(100)
y_sin = np.zeros(100)
for i in range(100):
    y_cos[i] = cos(x_values[i])
    y_sin[i] = sin(x_values[i])
    for j in range(n):
        y_values[i] += res[j] * (x_values[i] ** j)

plt.plot(x_values, y_values, 'bo-', label='Массивы ''x и y')
plt.plot(x_values, y_cos, 'r-', label='y = cos(x)')
#plt.plot(x_values, y_sin, 'r-', label='y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики массивов x и y, y = cos(x)')
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()