a=float(input("Nhap a = "))
b=float(input("Nhap b = "))
c=float(input("Nhap c = "))
d=float(input("Nhap d = "))
e=float(input("Nhap e = "))
max_f=a
min_f=a
if (b>max_f):
    max_f=b
if (c>max_f):
    max_f=c
if (d>max_f):
    max_f=d
if (e>max_f):
    max_f=e
    
if (b<min_f):
    min_f=b
if (c<min_f):
    min_f=c
if (d<min_f):
    min_f=d
if (e<min_f):
    min_f=e

print(f"So thuc lon nhat trong 3 so la: {max_f}")
print(f"So thuc nho nhat trong 3 so la: {min_f}")