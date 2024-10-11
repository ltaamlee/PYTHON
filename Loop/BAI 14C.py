#S=1/2+2/3+...+n/n+1
n=int(input("Nhap n = "))
s=0
i=1
while (i<=n):
    s+=i/(i+1)
    i+=1
print(round(s,2))

