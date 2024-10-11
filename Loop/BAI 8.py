max_n=float("-inf")
while True:
    n=int(input("Nhap n = "))
    if (n!=0):
        if (n>max_n):
            max_n=n
    else:
        break
print(f"So lon nhat trong cac so vua nhap la : {max_n}")
        