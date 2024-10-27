from math import pi

class Circle:
    def __init__(self, r):
        self.r=r

    def P(self):
        return 2*pi*self.r

    def A(self):
        return self.r**2*pi

    def PrintInfo(self):
        print(f"Hinh tron co: \nBan kinh R = {self.r}\nChu vi : {self.P()}\nDien tich : {self.A()}")

c=Circle(10)
c.PrintInfo()
