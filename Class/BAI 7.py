from GiaoDichTienTe import GiaoDichTienTe
from GiaoDichVang import GiaoDichVang
from QuanLyGiaoDich import QuanLyGiaoDich

danhSachGiaoDich = []
tongSoLuongGiaoDichVang = 0
tongSoLuongGiaoDichTienTe = 0
tongThanhTienGiaoDichVang = 0.0
tongThanhTienGiaoDichTienTe = 0.0

print("Nhap thong tin cac loai giao dich: ")
while True:
    loaiGiaoDich = input("Ban muon giao dich vang hay tien te (vang / tien te) (Nhan Enter de ket thuc viec nhap lieu): ")
    
    if loaiGiaoDich != "vang" and loaiGiaoDich != "tien te":
        break
    if loaiGiaoDich == "vang":
        tongSoLuongGiaoDichVang += 1
        x=GiaoDichVang()
        x.NhapThongTin()
        tongThanhTienGiaoDichVang+=x.ThanhTien()
    else:
        tongSoLuongGiaoDichTienTe+=1
        x=GiaoDichTienTe()
        x.NhapThongTin()
        tongThanhTienGiaoDichTienTe +=x.ThanhTien(x.loaiGiaoDich)

    danhSachGiaoDich.append(x)

print("Xuat thong tin cac loai giao dich: ")
for x in danhSachGiaoDich:
    x.XuatThongTin()

print("Tong so luong giao dich vang: ", tongSoLuongGiaoDichVang)
print("Tong so luong giao dich tien te: ", tongSoLuongGiaoDichTienTe)
print("Tong thanh tien giao dich vang: ", tongThanhTienGiaoDichVang)
print("Tong thanh vien giao dich tien te: ", tongThanhTienGiaoDichTienTe)