year=int(input("Nhap nam = "))
if ((year%400==0) or (year%100==0 and year%4==0)):
    print(f"{year} la nam nhuan!")
else:
    print(f"{year} khong la nam nhuan!")
    