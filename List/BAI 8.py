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
        
a=list(set(a))
print(f"List a: {a}")
