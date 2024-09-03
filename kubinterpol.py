from gauss import solve_gauss
from progon import thomas_algorithm
def cubic_spline_value(X, Y, point):
    n=len(X)
    h=[0]*(n-1)
    for i in range(0,n-1):
        h[i]=X[i+1]-X[i]
    #print(h)
    a=[0]*(n-2)
    b = [0] * (n - 2)
    c=[0]*(n-2)
    for i in range(0,n-2):
        a[i]=h[i]/6
        b[i] = (h[i] + h[i + 1]) / 3
        c[i] = h[i + 1] / 6
    #print(a)
    #print(b)
    #print(c)

    A=[0]*n
    for i in range(n):
        A[i]=[0,0,0,0,0]
    A[0][0]=-1/3.*1+1
    A[0][1]=-1*h[0]/6.
    A[1][0]=a[0]
    A[1][1]=b[0]
    A[1][2]=c[0]
    A[2][1]=a[1]
    A[2][2]=b[1]
    A[2][3]=c[1]
    A[3][2]=a[2]
    A[3][3]=b[2]
    A[3][4]=c[2]
    A[4][3]=1*h[3]/6
    A[4][4]=1+h[3]/3
    print("Матрица системы:")
    for i in range(0,n):
        print(A[i])

    d=[0]*n
    d[0]=9-1*(Y[1]-Y[0])/h[0]
    d[1]=(Y[2]-Y[1])/h[1]-(Y[1]-Y[0])/h[0]
    d[2]=(Y[3]-Y[2])/h[2]-(Y[2]-Y[1])/h[1]
    d[3]=(Y[4]-Y[3])/h[3]-(Y[3]-Y[2])/h[2]
    d[4]=144-1*(Y[4]-Y[3])/h[3]
    print(f"Свободный столбец коэф.: {d}")

    m=solve_gauss(A,d)
    print(f"Матрица коэф. m: {m}")

    for i in range(n):
        if point>X[i] and point<X[i+1]:
            znach=m[i]*(X[i+1]-point)**2/(6*h[n-2])+m[i+1]*(point-X[i])**2/(6*h[n-2])+(Y[i]-(m[i]*h[n-2]**2)/6)*(X[i+1]-point)/2+(Y[i+1]-(m[i+1]*h[n-2]**2)/6)*(point-X[i])/2
            print(f"Значение сплайна в точке {point} = {znach}")
    return 0.0


# Пример использования
X = [1, 2, 3, 4,6]
Y = [1, 8, 27, 64,216]
print("Массив X:",X)
print("Массив Y:",Y)
cubic_spline_value(X,Y,5)