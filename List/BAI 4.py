a=[]
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            x=float(input(f"a[{i+1}] = "))
            a.append(x)
        break
    else:
        print("Hay nhap n>=0 !")
b=[]
while True:
    k=int(input("Nhap k = "))
    if (k>0):
        for i in range(n):
            if (a[i]<0):
                b.append(i+1)
        if (len(b)>0 and k<=len(b)):
            print(f"Vi tri phan am thu {k} : {b[k-1]}")
        else:
            print(f"Khong co so am thu {k} trong list !")
        break
    else:
        print("Hay nhap k nguyen duong !")