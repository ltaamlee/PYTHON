n=int(input("Nhap n = "))
d={}
for i in range(1,n+1):
    d.update({i:i*i})
print(d)