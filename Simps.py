#TODO!! Спросить почему S0 = f0 + f1, что такое f0 & f1?

def f(x):
    return x**4  # Пример функции, замените на нужную вам функцию

a = float(input("Введите нижнюю границу интегрирования: "))
b = float(input("Введите врехнюю границу интегрирования: "))
n = int(input("Введите кол-во отрезков разбиения: "))
epsilon = float(input("Введите погрешность: ")) * 15/16

h = (b-a)/n
S0 = f(a) + f(b)
S1 = S2 = 0

for i in range(n):
    x = a + i*h
    if i % 2 != 0:
        S1 += f(x)
    else:
        S2 += f(x)

I1 = h/3 * (S0 + 4*S1 + 2*S2)

n *= 2
h /= 2
S1 = S2 = 0


for i in range(n):
    x = a + i*h
    if i % 2 != 0:
        S1 += f(x)

I2 = h/3 * (S0 + 4*S1 + 2*S2)

steps = 0

while abs(I2 - I1) > epsilon:
    I1 = I2
    n *= 2
    h /= 2
    S1 = S2 = 0
    for i in range(n):
        x = a + i * h
        if i % 2 != 0:
            S1 += f(x)
        else:
            S2 += f(x)
    I2 = h/3 * (S0 + 4 * S1 + 2 * S2)
    steps += 1

print('Шагов = ', steps)
print('Результат: ', I2)