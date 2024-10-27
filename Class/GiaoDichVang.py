from QuanLyGiaoDich import QuanLyGiaoDich
from datetime import datetime

class GiaoDichVang(QuanLyGiaoDich):
    def __init__(self, maGiaoDich, ngayGiaoDich, donGia, soLuong, loaiVang, loaiGiaoDich):
        self.maGiaoDich=maGiaoDich
        self.ngayGiaoDich=ngayGiaoDich
        self.donGia=donGia
        self.soLuong=soLuong
        self.loaiVang=loaiVang
        self.loaiGiaoDich=loaiGiaoDich

    
    def __init__(self):
        pass

    def NhapThongTin(self):
        self.maGiaoDich=input("Nhap ma giao dich: ")
        __date=input("Nhap ngay giao dich (dd/MM/yyyy): ")
        self.ngayGiaoDich = datetime.strptime(__date, "%d/%m/%Y")
        while True:
            try:
                self.donGia = float(input("Nhap don gia: "))
                break
            except ValueError:
                print("Don gia phai la mot so! Vui long nhap lai!")

        while True:
            try:
                self.soLuong= int(input("Nhap so luong: "))
                break
            except ValueError:
                print("So luong phai la mot so tu nhien, vui long nhap lai!")

        self.loaiVang = ""
        while self.loaiVang != "18k" and self.loaiVang != "24k" and self.loaiVang != "9999":
            self.loaiVang = input("Nhap loai vang (18k / 24k / 9999): ").lower()
            if self.loaiVang != "18k" and self.loaiVang != "24k" and self.loaiVang != "9999":
                print("Loai vang chi bao gom cac loai 18k, 24k hoac 9999")
     
    def ThanhTien(self):
        return self.soLuong * self.donGia
    def XuatThongTin(self):
        print(f"Thong tin giao dich vang:\n+ Ma giao dich: {self.maGiaoDich}\n+ Ngay giao dich: {self.ngayGiaoDich.strftime('d/%m/%Y')}\n+ Don gia: {self.donGia}\n+ Loai vang: {self.loaiVang}\n+ Thanh tien: {self.ThanhTien()}")