from math import sin,pi
#n=int(input("Введите степень полинома:\n"))
print("Ввод массива Х:")
#X = [float(input()) for n in range(n+1)]
XX=[0,pi/6,pi/4,pi/3]
print(XX)

print("Ввод массива Y:")
#Y = [float(input()) for n in range(n+1)]
YY=[sin(0),sin(pi/6),sin(pi/4),sin(pi/3)]
print(YY)

def razd(X,Y):

    for i in range(1,len(X)):
        for j in range(len(X)-1,i-1,-1):
            Y[j]=((Y[j]-Y[j-1])/(X[j]-X[j-i]))


def newton(x,X,Y):
    sum=0
    for i in range(0,len(X)):
        pr=1
        for j in range(i):
            pr*=x-X[j]
        sum+=pr*Y[i]
        print(sum)
    return True



razd(XX,YY)
#= 0.5645550613332508
print("Значения полинома ньютона нарастающих степенней в точке:")
print(newton(1,XX,YY))
print("Значение функции в точке")
print(sin(1))
