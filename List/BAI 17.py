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

max_a=a[0]
min_a=a[0]
for i in a:
    if (i<min_a):
        min_a=i
    if (i>max_a):
        max_a=i
        
print(f"So lon nhat cua list = {max_a}")
print(f"So nho nhat cua list = {min_a}")
