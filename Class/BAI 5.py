from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def P(self):
        pass
    
    @abstractmethod
    def A(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def P(self):
        return 2 * pi * self.r

    def A(self):
        return pi * self.r**2

class Rectangle(Shape):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def P(self):
        return (self.dai + self.rong) * 2

    def A(self):
        return self.dai * self.rong

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def IsTriangle(self):
        if (self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a):
            return True

        return False

    def P(self):
        return self.a + self.b + self.c

    def A(self):
        p=self.P()/2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

c=Circle(12)
r=Rectangle(4, 12)
t=Triangle(6, 8, 10)

print("Chu vi hinh tron: ", c.P())
print("Dien tich hinh tron: ", c.A())

print("Chu vi hinh chu nhat: ", r.P())
print("Dien tich hinh chu nhat: ", r.A())

if t.IsTriangle():
    print("Chu vi hinh tam giac: ", t.P())
    print("Dien tich hinh tam giac: ", t.A())
else:
    print("Day khong phai do dai 3 canh cua 1 tam giac!")