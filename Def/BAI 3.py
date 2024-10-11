from math import sqrt

def isPrime(x):
    if (x<2):
        return False
    for i in range(2, int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True


n=int(input("Nhap n = "))
if (isPrime(n)):
    print(f"{n} la so nguyen to ")
else:
    print(f"{n} khong la so nguyen to ")