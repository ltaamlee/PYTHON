import math
def CHECK(n):
    return (((math.sin(n)**2)+(math.cos(n)**2))==1)
x=math.pi
print(CHECK(x))

x=(math.pi)/2
print(CHECK(x))

x=(math.pi)*(4/3)
print(CHECK(x))