import numpy as np
import matplotlib.pyplot as plt

# Данные
x = np.array([0,1, 2, 3, 4])
y = np.array([0,11,22,-4,5])

# Веса
weights = np.array([1, 1, 1, 1, 1])  # Пример весов
weights2 = np.array([1, 1, 2, 1, 1])
# Подгоняем полином 3-й степени к данным
coefficients = np.polyfit(x, y, 3, w=np.sqrt(weights))
coefficients2 = np.polyfit(x, y, 3, w=np.sqrt(weights2))

# Создаем полиномиальную функцию
poly_func = np.poly1d(coefficients)
print(poly_func)

poly_func2 = np.poly1d(coefficients2)
print(poly_func2)

XX=np.linspace(0, 4, 100)

# Строим график
plt.scatter(x, y, label='Данные')
plt.plot(XX, poly_func(XX), color='red', label='Полином 3-й степени с 1 вес коэф')
plt.plot(XX, poly_func2(XX), color='green', label='Полином 3-й степени, притягивание к 3 точке')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Полиномиальная регрессия 3-й степени с весами')
plt.legend()
plt.grid(True)
plt.show()
