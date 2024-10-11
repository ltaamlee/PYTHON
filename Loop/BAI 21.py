from math import sqrt
def SNT(x):
    if (x<2):
        return False
    for i in range (2,int(sqrt(x))+1):
        if (x%i==0):
            return False
    return True

n=int(input("Nhap n = "))
i=2
cnt=0
a=[]
while (cnt<n):
    if (SNT(i)):
        a.append(i)
        cnt+=1
    i+=1
print(a)