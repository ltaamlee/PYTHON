from math import sqrt

class TamGiac:
    def __init__(self, a, b, c, color):
        self.a=a
        self.b=b
        self.c=c
        self.color=color

    def get_a(self):
        return a
    
    def set_a(self, value):
        self.a=value

    def get_b(self):
        return b
    
    def set_b(self, value):
        self.b=value

    def get_c(self):
        return c
    
    def set_c(self, value):
        self.c=value

    def get_color(self):
        return color
    
    def set_color(self, value):
        self.color= value

    def ChuVi(self):
        return self.a + self.b + self.c

    def DienTich(self):
        p=self.ChuVi()/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def IsTamGiac(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            return True
        else:
            return False

    def LoaiTamGiac(self):
        if not (self.IsTamGiac()):
            return "khong phai la 3 canh cua 1 tam giac"
        else:
            if self.a == self.b and self.a == self.c:
                return "la tam giac deu"
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                if self.a == sqrt(self.b**2 + self.c**2) or self.b == sqrt(self.c**2 + self.a**2) or self.c == sqrt(self.a**2 + self.b**2):
                    return "la tam giac vuong can"
                else:
                    return "tam giac can"
            elif self.a == sqrt(self.b**2 + self.c**2) or self.b == sqrt(self.c**2 + self.a**2) or self.c == sqrt(self.a**2 + self.b**2):
                return "la tam giac vuong"
            else:
                return "la tam giac thuong"

    def PrintInfo(self):
        print("3 canh nay " + self.LoaiTamGiac())
        if self.IsTamGiac():
            print("Chu vi cua tam giac: ", self.ChuVi())
            print("Dien tich cua tam giac: ", self.DienTich())
            print("Mau sac cua tam giac: ", self.color)

triangle=TamGiac(3,4,5,"green")
triangle.PrintInfo()