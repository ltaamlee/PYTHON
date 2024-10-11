def STAR(p):
    if (p<2):
        return 5
    elif (2<=p and p<4):
        return 4
    elif (4<=p and p<6):
        return 3
    elif (6<=p and p<10):
        return 2
    elif (p>=10):
        return 1

P=int(input("Nhap luong dien nang tieu thu moi ngay (kWh) = "))
print(f"So sao tiet kiem nang luong : {STAR(P)}")
    
