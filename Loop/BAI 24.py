from math import sqrt
import decimal
from decimal import Decimal

def DIS(a,b):
    return sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)

point=[]

x=input("Enter the first x-coordinate: ")
y=input("Enter the first y-coordinate: ")
point.append((float(x),float(y)))

while True:
    x=input("Enter the next x-coordinate (blank to quit): ")
    if (x==""):
        break
    y=input("Enter the next y-coordinate (blank to quit): ")
    point.append((float(x),float(y)))

per=0
for i in range (0,len(point)-1):
    per+=DIS(point[i],point[i+1])
    
per=per+(DIS(point[0],point[len(point)-1]))

decimal.getcontext().prec=13
print(Decimal(per)/1)