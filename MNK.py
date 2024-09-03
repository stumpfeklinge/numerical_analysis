from math import sin, pi
from gauss import solve_gauss
import matplotlib.pyplot as plt
import numpy as np

#XX=[0,pi/6,pi/4,pi/3,1]
#YY=[sin(0),sin(pi/6),sin(pi/4),sin(pi/3),sin(1)]

XX=[0,1,2,3,4]
YY=[0,11,22,-4,5]
ves=[1,1,2,1,1]

n=len(XX)
G=[0]*n
for i in range(n):
    G[i]=[0]*n
for i in range(n):
    for j in range(n):
        suma=0
        for k in range(n):
            suma+=XX[k]**(i+j)
        G[i][j]=suma


d=[0]*n
for i in range(n):
    suma=0
    for k in range(n):
        suma+=YY[k]*XX[k]**i
    d[i]=suma

m=int(input("Введите степень многочлена: \n"))+1
GG=[0]*m
dd=[0]*m
for i in range(m):
    GG[i]=[0]*m
for i in range(m):
    dd[i]=d[i]
    for j in range(m):
        GG[i][j]=G[i][j]
print("Система для многочлена наибольшей степени:")
for i in range(n):
    print(G[i]," ",d[i])
print(f"Система для многочлена {m-1} степени")
for i in range(m):
    print(GG[i]," ",dd[i])

print("Коэф. для многочлена наибольшей степени:")
Xmax=solve_gauss(G,d)
print(Xmax)
def Maxi(x,Xmax):
    s=0
    for i in range(len(Xmax)):
        s+=Xmax[i]*(x**i)
    return s

print(f"Коэф. для многочлена степени {m-1}:")
Xvash=solve_gauss(GG,dd)
print(Xvash)

def Nash(x,Xvash):
    s=0
    for i in range(len(Xvash)):
        s+=Xvash[i]*(x**i)
    return s

x_values = np.array([i / 25 for i in range(0,100)])*ves[k]
y_max = np.zeros(100)
y_nash = np.zeros(100)
for i in range(100):
    y_nash[i] = Nash(x_values[i],Xvash)
    y_max[i] = Maxi(x_values[i],Xmax)

plt.plot(x_values, y_nash,color='green', label=f'Многочлен {m-1} степени')
plt.plot(x_values, y_max, 'r-', label=f'Многочлен {n-1} степени')
plt.plot(XX,YY,'bo',label='Массивы ''x и y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики')
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()