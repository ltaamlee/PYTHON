try:
    x=float(input("Nhap so thuc x = "))
    if (x>0):
        print("x^2 + 3x +5 =".x*x+3*x+5)
    else:
        print("-x^2 - 3x - 5 =",-(x*x)-3*x-5)
except ValueError:
    print("Gia tri x khong hop le!")
