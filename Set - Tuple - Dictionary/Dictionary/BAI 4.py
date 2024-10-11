n=int(input("Nhap n = "))
a=[]
b=[]
mydict={}

print("Nhap cac phan tu cua list A: ")
for i in range(n):
    a.append(int(input()))
print("Nhap cac phan tu cua list B: ")
for i in range(n):
    b.append(int(input()))

for i in range(n):
    mydict.update({a[i]:b[i]})

print(mydict)