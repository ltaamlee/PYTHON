from math import sqrt

class Point:
    def __init__(self, x, y, color):
        self.x=x
        self.y=y
        self.color=color

    def PrintInfo(self):
        print("Thong tin cua diem: ")
        print("    + Hoanh do: ", self.x)
        print("    + Tung do: ", self.y)
        print("    + Mau sac: ", self.color)

    def Move(self, x, y = 0):
        self.x+=x
        self.y+=y
    
    def Distance(self, d = None):
        if d == None:
            return sqrt(self.x**2 + self.y**2)

        return sqrt((self.x-d.x)**2 + (self.y-d.y)**2)

point = Point(12, 15, "Blue")
point.PrintInfo()
point.Move(15)
print("Thong tin cua diem sau khi tinh tien 15 buoc theo hoanh do: ")
point.PrintInfo()

point.Move(20, 20)
print("Thong tin cua diem sau khi tinh tien 20 buoc theo ca hoanh do va tung do: ")
point.PrintInfo()

print("Khoang cach giua diem va goc toa do: ", point.Distance())
d = Point(10, 13, "blue")
print("Khoang cach giua diem va diem d(10,13): ", point.Distance(d))