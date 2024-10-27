class Course:
    def __init__(self, maMon, tenMon, soTiet):
        self.maMon = maMon
        self.tenMon = tenMon
        self.soTiet = soTiet

    def GetTenMon(self):
        return self.tenMon

    def ToString(self):
        return f"+ Ma mon: {self.maMon}\n+ Ten mon: {self.tenMon}\n+ So tiet: {self.soTiet}"

class Student:
    def __init__(self, iD, name, birthyear, listCourse):
        self.iD = iD
        self.name = name
        self.birthyear = birthyear
        self.listCourse = listCourse

    def __ListCourseToString(self):
        string = ""
        for subj in self.listCourse:
            string += subj.ToString() + " "
        return string

    def ToString(self):
        stringListCourse = self.__ListCourseToString()
        return f"+ Ma so hoc vien: {self.iD}\n+ Ten hoc vien: {self.name}\n+ Nam sinh: {self.birthyear}\n+ Danh sach mon hoc dang ky: {stringListCourse}"

danhSachHocVien = []
danhSachMonHoc = []
with open("dssv.txt", 'w', encoding = 'utf-8') as file:
    while True:	
        lstCourse = []
        print("Nhap thong tin hoc vien (Ket thuc bang cach nhan enter ma khong nhap ma so hoc vien): ")

        iD = input("Nhap ma so hoc vien: ")
        if (iD == ""):
            break

        name = input("Nhap ten hoc vien: ")

        while True:
            try:
                birthyear = int(input("Nhap nam sinh: "))
                break
            except ValueError:
                print("Ngay sinh phai la mot so nguyen duong, vui long nhap lai!")

        file.write(iD + '\n')
        file.write(name + '\n')
        file.write(str(birthyear) + '\n')

        numSubj = int(input("Nhap so mon hoc hoc vien dang ky: "))
        for i in range(numSubj):
            maMon = input("Nhap ma mon: ")
            tenMon = input("Nhap ten mon: ")
            
            while True:
                try:
                    soTiet = int(input("Nhap so tiet: "))
                    break
                except ValueError:
                    print("So tiet phai la mot so nguyen duong, vui long nhap lai!")
            
            file.write(maMon + "\n")
            file.write(tenMon + "\n")
            file.write(str(soTiet) + "\n")

            subj = Course(maMon, tenMon, soTiet)
            lstCourse.append(subj)
            danhSachMonHoc.append(subj)

        student = Student(iD, name, birthyear, lstCourse)
        danhSachHocVien.append(student)

print("Thong tin cac hoc vien dang ki tai trung tam: ")
for student in danhSachHocVien:
    print(student.ToString())

flag = False
print(f"Thong tin cac hoc vien dang ki it nhat 2 mon hoc: ")
for student in danhSachHocVien:
    if len(student.listCourse) >= 2:
        print(student.ToString())
        flag = True
if flag == False:
    print("Du lieu khong ton tai!")

counter = {}
for monHoc in danhSachMonHoc:
    if monHoc.maMon not in counter:
        counter[monHoc.maMon] = 1
    else:
        counter[monHoc.maMon] += 1

maxValue = 0
maxMaMon = ""
for subj, value in counter.items():
    if maxValue < value:
        maxValue = value
        maxMaMon = subj

#Tra ma mon
maxSubj = []
for subj in danhSachMonHoc:
    if maxMaMon == subj.maMon:
        maxSubj = subj
        break

print(f"Thong tin mon hoc duoc nhieu hoc vien dang ky nhat la {maxMaMon} voi {maxValue} luot dang ky:")
print(maxSubj.ToString())

print(f"Thong ke so luong hoc vien trong moi mon hoc: ")
for maMon, soLuong in counter.items():
    for subj in danhSachMonHoc:
        if subj.maMon == maMon:
            print(f"+ Ma mon hoc: {subj.maMon}\n+ Ten mon hoc: {subj.tenMon}\n+ So luong hoc vien dang ky: {soLuong}")
            break
