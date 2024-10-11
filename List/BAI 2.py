a=[]
s=0.0
while True:
    n=int(input("N = "))
    if n>0:
        for i in range(n):
            x=float(input(f"a[{i+1}] = "))
            a.append(x)
        break
    elif (n==0):
        print("Trung binh cong cua list = 0")
        break
    else:
        print("Hay nhap n>=0 !")
for i in a:
    s+=i
print(f"Trung binh cong cua list = {s/n}")
