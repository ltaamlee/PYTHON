def SUM(x):
    ss=0
    i=1
    while (i<=x):
        ss+=i
        i+=1
    return ss
n=int(input("Nhap n = "))
s=0
for i in range(1,n+1):
    s+=1/(SUM(i))
print(round(s,2))
