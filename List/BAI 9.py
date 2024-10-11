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
a.sort()
print(f"Mang sau khi sap xep tang dan: {a}")