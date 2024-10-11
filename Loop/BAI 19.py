a=[4,12,5,20,11]
b=[]
print("List ban dau:")
for i in a:
    print(i," ",end="")
print()
A=int(input("Nhap A = "))
print("List sau khi xoa cac phan tu lon hon A:")
for i in a:
    if (i<A):
        b.append(i)
for i in b:
    print(i," ",end="")
