a=[]
s=0.0
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            x=float(input(f"a[{i+1}] = "))
            a.append(x)
        break
    else:
        print("Hay nhap n>=0 !")
for i in a:
    s+=i
print(f"Tong cac phan tu cua list = {s}")
