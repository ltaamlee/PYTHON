a=[]
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            x=int(input(f"a[{i+1}] = "))
            a.append(x)
        break
    else:
        print("Hay nhap n>=0 !")

while True:
    k=int(input("Nhap k = "))
    if (k>=0):
        break
    else:
        print("Hay nhap k >=0 !")
        
a=[i for i in a if i!=k]

if (len(a)==n):
        print(f"Phan tu {k} khong ton tai trong list !")
print(f"List a: {a}")