a=float(input("Nhap a = "))
b=float(input("Nhap b = "))
c=float(input("Nhap c = "))
print("Cac so co tri tuyet doi nho hon 10: ")
check=False
if (abs(a)<10):
    print(a)
    check=True
if (abs(b)<10):
    print(b)
    check=True
if (abs(c)<10):
    print(c)
    check=True
if (check==False):
    print("Khong co!")

