from QuanLyGiaoDich import QuanLyGiaoDich
from datetime import datetime

class GiaoDichTienTe(QuanLyGiaoDich):
    def __init__(self, maGiaoDich, ngayGiaoDich, donGia, soLuong, loaiTienTe, loaiGiaoDich):
        self.maGiaoDich=maGiaoDich
        self.ngayGiaoDich=ngayGiaoDich
        self.donGia=donGia
        self.soLuong=soLuong
        self.loaiTienTe=loaiTienTe
        self.loaiGiaoDich=loaiGiaoDich
    
    def __init__(self):
        pass

    def NhapThongTin(self):
        self.maGiaoDich=input("Nhap ma giao dich: ")
        __date=input("Nhap ngay giao dich (dd/MM/yyyy): ")
        self.ngayGiaoDich=datetime.strptime(__date, "%d/%m/%Y")
        while True:
            try:
                self.donGia=float(input("Nhap ty gia: "))
                break
            except ValueError:
                print("Ty gia phai la mot so! Vui long nhap lai!")

        while True:
            try:
                self.soLuong=int(input("Nhap so luong: "))
                break
            except ValueError:
                print("So luong phai la mot so tu nhien, vui long nhap lai!")
        
        self.loaiTienTe=""
        while self.loaiTienTe != "USD" and self.loaiTienTe != "EUR" and self.loaiTienTe != "AUR":
            self.loaiTienTe=input("Nhap loai tien te (USD / EUR / AUR): ").upper()
            if self.loaiTienTe != "USD" and self.loaiTienTe != "EUR" and self.loaiTienTe != "AUR":
                print("Tien te chi bao gom cac don vi USD / EUR / AUR")
        
        self.loaiGiaoDich = ""
        while self.loaiGiaoDich != "mua" and self.loaiGiaoDich != "ban":
            self.loaiGiaoDich=input("Nhap loai giao dich (mua / ban): ").lower()
            if self.loaiGiaoDich != "mua" and self.loaiGiaoDich != "ban":
                print("Loai giao dich chi bao gom mua hoac ban") 
    
    def XuatThongTin(self):
        print(f"Thong tin giao dich tien te:\n+ Ma giao dich: {self.maGiaoDich}\n+ Ngay giao dich: {self.ngayGiaoDich.strftime('%d/%m/%Y')}\n+ Don gia: {self.donGia}\n+ Loai tien te: {self.loaiTienTe}\n+ Thanh tien: {self.ThanhTien(self.loaiGiaoDich)}")    
    def ThanhTien(self, loaiGiaoDich):
        if loaiGiaoDich == "mua":
            return self.soLuong*self.donGia
        else:
            return (self.soLuong*self.donGia)*1.05