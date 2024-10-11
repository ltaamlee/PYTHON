#S=1/1*2 + 1/2*3 +...+1/n*(n+1)
n=int(input("Nhap n = "))
s=0
i=1
while (i<=n):
    s+=1/(i*(i+1))
    i+=1
print(round(s,2))

