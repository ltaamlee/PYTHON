from math import floor
year=int(input("Nhap nam = "))
day=(year+floor((year-1)/4)-floor((year-1)/100)+floor((year-1)/400))%7
print(f"Ngay 1 thang 1 nam {year} la ",end="")
if (day==0):
    print("Chu Nhat")
if (day==1):
    print("Thu Hai")
if (day==2):
    print("Thu Ba")
if (day==3):
    print("Thu Tu")
if (day==4):
    print("Thu Nam")
if (day==5):
    print("Thu Sau")
if (day==6):
    print("Thu Bay")