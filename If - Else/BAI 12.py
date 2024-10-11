try:
    a=int(input("Nhap a = "))
    b=int(input("Nhap b = "))
    if (a%b==0):
        print(f"{a} la boi so cua {b}")
    else:
        print(f"{a} KHONG la boi so cua {b}")
except ValueError:
    print("Gia tri a hoac b khong hop le!")