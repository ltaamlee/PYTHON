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

for i in range(n-1):
    for j in range(i+1,n):
        if (a[i]%2==0):
            if (a[j]%2==0 and a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
        else:
            if (a[j]%2!=0 and a[i]<a[j]):
                a[i],a[j]=a[j],a[i]
                
print(f"Mang sau khi sap xep cac phan tu le giam dan, phan tu chan tang dan: \n {a}")

