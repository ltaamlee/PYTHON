#S=1/1*2 + 1/2*3 +...+1/n*(n+1)
n=int(input("Nhap n = "))
s=0
for i in range (1,n+1):
    s+=1/(i*(i+1))
print(round(s,2))
