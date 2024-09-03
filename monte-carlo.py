from math import sin,cos,pi
import random
#Первый вариант расчета интеграла.
def F(x,y):
	return sin(pi*x)*cos((pi*y)/2)

N = int(input('Введите количество значений равномерно распределенной случайной величины:'))
sum_integral = 0
'''
1 metod
'''## $$\int_0^1\int_0^1sin(pi*x)*cos((pi*y)/2)\mathrm{d}x\mathrm{d}y $$
print("Случайные точки из области интегрирования:")
for i in range(N):
	x = random.random()
	y = random.random()
	sum_integral += F(x,y)
	print(x,' ',sum_integral)
rezult = sum_integral/N
print('Результат для случайных величин ( 1 метод ):',rezult)
print()
'''
2 metod
'''
print("Случайные точки из области интегрирования:")
count_point = 0
for i in range(N):
	x = random.random()
	y = random.random()
	z = random.random()
	if z <= F(x,y):
		count_point+=1
	print(x,' ',sum_integral)
print('Результат для случайных величин ( 2 метод ):',count_point/N)
print()
print('Посчитанный результат:',4/(pi*pi))
print()