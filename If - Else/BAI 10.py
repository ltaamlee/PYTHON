a=int(input("Nhap a = "))
b=int(input("Nhap b = "))
c=int(input("Nhap c = "))
d=int(input("Nhap d = "))
e=int(input("Nhap e = "))
pos=0
neg=0
zero=0
if (a>0):
    pos+=1
elif (a<0):
    neg+=1
else:
    zero+=1

if (b>0):
    pos+=1
elif (b<0):
    neg+=1
else:
    zero+=1

if (c>0):
    pos+=1
elif (c<0):
    neg+=1
else:
    zero+=1
    
if (d>0):
    pos+=1
elif (d<0):
    neg+=1
else:
    zero+=1
    
if (e>0):
    pos+=1
elif (e<0):
    neg+=1
else:
    zero+=1
    
print(f"Co {pos} so duong")
print(f"Co {neg} so am")
print(f"Co {zero} so 0")