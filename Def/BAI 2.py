def trungvi(a,b,c):
    l=[a,b,c]
    l.sort()
    print(l[1])

print("Nhap 3 diem a, b, c : ")
a=int(input())
b=int(input())
c=int(input())
print("Trung vi cua 3 diem : ",end="")
trungvi(a,b,c)