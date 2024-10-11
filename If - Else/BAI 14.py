a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
max_even=float("-inf")
if (a%2==0 and a>max_even):
    max_even=a
if (b%2==0 and b>max_even):
    max_even=b
if (c%2==0 and c>max_even):
    max_even=c
if (max_even==float("-inf")):
    print("Khong co so chan nao trong 3 so!")
else:
    print(f"So chan lon nhat la: {max_even}")