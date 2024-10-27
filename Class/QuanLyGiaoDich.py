import datetime

class QuanLyGiaoDich:
    def __init__(self, maGiaoDich, ngayGiaoDich, donGia, soLuong):
        self.maGiaoDich=maGiaoDich
        self.ngayGiaoDich=ngayGiaoDich
        self.donGia=donGia
        self.soLuong=soLuong

    def ThanhTien(self):
        return self.soLuong*self.donGia