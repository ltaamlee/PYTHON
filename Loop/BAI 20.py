a=[4,5,11,12,20]
b=float(input("Nhap so thuc B = "))
n=len(a)
for i in range (0,n):
    if (a[i]>b):
        a.insert(i,b)
        break
print(a)