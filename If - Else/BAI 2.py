rating=float(input("Nhap danh gia = "))
if (rating==0.0):
    print("Unacceptable Performance")
elif (rating==0.4):
    print("Acceptable Performance")
    print(2400*0.4)
elif (rating>=0.6):
    print("Meritorious Performance")
    print(2400*n)
else:
    print("Vui long nhap lai")