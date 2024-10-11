a=[]
pos=-1
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            x=float(input(f"a[{i+1}] = "))
            a.append(x)
        for i in range(len(a)):
            if (a[i]<0):
                pos=i
                break
        break
    else:
        print("Hay nhap n>=0 !")

if (pos!=-1):
    print(f"Vi tri phan tu am dau tien la {pos+1}")
else:
    print("List khong co phan tu am !")