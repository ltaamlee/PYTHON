while True:
    month=int(input("Nhap thang trong nam = "))
    if (1<=month and month<=12):
        if (month in [1,2,3]):
            season="Xuan"
        if (month in [4,5,6]):
            season="Ha"
        if (month in [7,8,9]):
            season="Thu"
        if (month in [10,11,12]):
            season="Dong"
        print(f"Thang {month} thuoc mua {season}")
        break
    else:
        print("Hay nhap thang tu 1 den 12 !")