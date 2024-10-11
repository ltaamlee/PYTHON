dg=int(input("Nhap don gia: "))
sl=int(input("Nhap soLuong: "))
tax=0.1
t=dg*sl
s=t*tax
print("{0:>26} {1:>1}*{2:>1}={3:>3}".format("Tong tien truoc thue: ",dg,sl,t))
print("{0:>25} {1:>12}".format("Tien thue:",s))
print("{0:>25} {1:>12}".format("Tong tien sau thue:",s+t))
