from BAI2D import gen_num, PT_BAC2, sort_increase, sort_decrease

print("Tao day so ngay nhien")
n=int(input("Nhap so luong phan tu : "))
Min=int(input("Nhap gia tri Min : "))
Max=int(input("Nhap gia tri Max : "))

res=gen_num(n,Min,Max)
print(f"Day so ngau nhien trong khoang [{Min}..{Max}] : ",res)

print("\n")
print("Giai phuong trinh bac 2")
a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
print(PT_BAC2(a,b,c))

print("\n")
l=[]
n=int(input("Nhap so luong phan tu cua mang = "))
for i in range(n):
    l.append(int(input(f"a[{i}] = ")))
    
print(f"Sap xep mang tang dan : {sort_increase(l)}")

print(f"Sap xep mang giam dan : {sort_decrease(l)}")