#S=1/2+3/4+...+2n+1/2n+2
n=int(input("Nhap n = "))
s=0
for i in range (0,n+1):
    s+=((2*i)+1)/((2*i)+2)
print(round(s,2))



