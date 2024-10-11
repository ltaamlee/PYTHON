from math import sqrt

def isPrime(x):
    if (x<2):
        return False
    for i in range(2, int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True

a=[]
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            a.append(int(input(f"a[{i+1}] = ")))   
        break     
    else:
        print("Hay nhap n >= 0 !")        

print("List cac so nguyen to: ",end="")
cnt=0
for i in a:
    if (isPrime(i)==True):
        print(i,end=" ")
        cnt+=1
if (cnt==0):
    print("Khong co so nguyen to trong list !")
