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
    
def SAVING(e):
    if (STAR(e)>3):
        return "Thiet bi nay tiet kiem dien !"
    else:
        return "Thiet bi nay khong tiet kiem dien !"
    
E=int(input("Nhap luong dien nang tieu thu moi ngay (kWh) = "))
print(SAVING(E))