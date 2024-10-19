class SV:
    def __init__(self, sv_id, name):
        self.sv_id = sv_id
        self.name = name
        
class QL:
    def __init__(self):
        self.sv=[]
        
    def ADD(self, sv_id, name):
        new_sv=SV(sv_id,name)
        self.sv.append(new_sv)
        
    def DEL(self, sv_id):
        for i in self.sv:
            if (i.sv_id==sv_id):
                self.sv.remove(i)
                return
        print("Khong tim thay sinh vien !")
        
    def EDIT(self, sv_id, new_name):
        for i in self.sv:
            if (i.sv_id==sv_id):
                i.name=new_name
                return
        print("Khong tim thay sinh vien !")
        
    def PRINT(self):
        if not self.sv:
            print("Danh sach rong !")
        else:
            for i in self.sv:
                print(f"MSSV: {i.sv_id}    Ten: {i.name}")
 
manager=QL()
while True:
    print("\n")
    print("CHUONG TRINH QUAN LI SINH VIEN")
    print("1. Them sinh vien")
    print("2. Xoa sinh vien")
    print("3. Sua sinh vien")
    print("4. Xem danh sach sinh vien")
    print("0. Thoat chuong trinh")
    
    key=int(input("Nhap lua chon : "))
    if key==1:
        ms=input("Nhap ma so sinh vien : ")
        ten=input("Nhap ho ten sinh vien : ")
        manager.ADD(ms,ten)
    elif key==2:
        ms=input("Nhap ma so sinh vien : ")
        manager.DEL(ms)
    elif key==3:
        ms=input("Nhap ma so sinh vien : ")
        ten=input("Nhap ho ten sinh vien can sua : ")
        manager.EDIT(ms,ten)
    elif key==4:
        manager.PRINT()
    elif key==0:
        print("Ket thuc chuong trinh !")
        break
    else:
        print("Lua chon khong ton tai trong chuong trinh !")