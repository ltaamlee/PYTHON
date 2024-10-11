from math import sqrt

def isPrime(x):
    if (x<2):
        return False
    for i in range(2, int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True

def nextPrime(n):
    while True:
        n+=1
        if (isPrime(n)):
            return n
    
n=int(input("Nhap n = "))
print(f"So nguyen to dau tien lon hon {n} : {nextPrime(n)}")