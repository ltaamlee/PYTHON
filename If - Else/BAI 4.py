from math import sqrt
a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
if (a==0):
    if (b==0):
        if (c==0):
            print("Phuong trinh vo so nghiem !")
        else:
            print("Phuong trinh vo nghiem !")
    else:
        if (c==0):
            print("Phuong trinh co 1 nghiem x = 0")
        else:
            print("Phuong trinh co 1 nghiem x =",-c/b)
else:
        delta=b*b-4*a*c
        if delta<0:
            print("Phuong trinh vo nghiem !")
        elif delta==0:
            print("Phuong trinh co nghiem kep: x =",round(-b/(2*a),2))
        else:
            print("Phuong trinh 2 co nghiem phan biet:")
            print("x1 =",round((-b+sqrt(delta))/(2*a),2))
            print("x2 =",round((-b-sqrt(delta))/(2*a),2))