a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
min_pos=float("inf")
if (a>0 and a<min_pos):
    min_pos=a
if (b>0 and b<min_pos):
    min_pos=b
if (c>0 and c<min_pos):
    min_pos=c
if (min_pos==float("inf")):
    print("Khong co so duong nao trong 3 so!")
else:
    print(f"So duong nho nhat la: {min_pos}")