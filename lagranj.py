from math import factorial,pi,sin

def Lag(x, X,Y,n):
    sum=0
    for i in range(0,n+1):
        pr=1
        for j in range(0,n+1):
            if j!=i:
                pr*=(x - X[j]) / (X[i] - X[j])
        sum+=Y[i]*pr
    return sum

def W(x,X,n):
    pr=1
    for i in range(0,n):
        pr*=(x-X[i])
    return pr


#n=int(input("Введите степень полинома:\n"))
#print("Ввод массива Х:")
#X = [float(input()) for n in range(n+1)]
#print("Ввод массива Y:")
#Y = [float(input()) for n in range(n+1)]
XX=[0,pi/6,pi/4,pi/3]
YY=[sin(0),sin(pi/6),sin(pi/4),sin(pi/3)]
n=len(XX)-1
M=int(input("Введите константу М:\n"))
tochka=float(input("Введите точку:\n"))
print("Значение полинома в точке =",Lag(tochka,XX,YY,n))

print("Оценка: ",W(tochka,XX,n+1)*M/factorial(n+1))

print("Значение начальной функции в точке =",sin(tochka))