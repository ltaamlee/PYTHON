while True:
    a=int(input("Nhap tu so = "))
    b=int(input("Nhap mau so = "))
    if (a!=0 and b!=0):
        p=a/b
        print("{:.3f}".format(p))
    else:
        break