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
u=[]
b=[]
while True:
    k=int(input("Nhap k = "))
    if (k>=0):
        for i in a:
            if (i!=0 and k%i==0):
                u.append(i)
            if (k!=0 and i%k==0):
                b.append(i)
        break
    else:
        print("Hay nhap k >=0 !")
        
if (len(u)>0):
    print(f"Cac so la uoc cua {k}: {[i for i in u]}")
else:
    print(f"Khong co so nao la uoc cua {k} !")
    
if (len(b)>0):
    print(f"Cac so la boi cua {k}: {[i for i in b]}")
else:
    print(f"Khong co so nao la boi cua {k} !")
