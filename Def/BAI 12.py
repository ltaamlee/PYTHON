def TAYLOR(x):
    c= 1.0
    fact= 1.0
    sign = -1
    
    for i in range(2, 100, 2):
        fact*=i*(i-1)  
        c+=sign*(x**i)/fact
        sign*=-1  

    return c

x=int(input("Nhap x (radian) = "))
print(f"cos(x) theo Taylor = {TAYLOR(x)}")
