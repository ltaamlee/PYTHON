from ptbac2 import PT_BAC2
from sortincr import sort_increase
from sortdecr import sort_decrease

print("Giai phuong trinh bac 2")
a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
print(PT_BAC2(a,b,c))

l=[]
n=int(input("Nhap so luong phan tu cua mang = "))
for i in range(n):
    l.append(int(input(f"a[{i}] = ")))
    
print(f"Sap xep mang tang dan : {sort_increase(l)}")

print(f"Sap xep mang giam dan : {sort_decrease(l)}")