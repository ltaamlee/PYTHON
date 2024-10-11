def SAVING(e):
    if (e<10):
        return "Thiet bi nay tiet kiem dien !"
    else:
        return "Thiet bi nay khong tiet kiem dien !"

E=int(input("Nhap luong dien nang tieu thu moi ngay (kWh) = "))
print(SAVING(E))