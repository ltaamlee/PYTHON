n=int(input("Nhap so luong hoc sinh = "))
d={}

for i in range(n):
    mark=float(input("Nhap diem = "))
    name=input("Nhap ten = ")
    d.update({mark:name})
    
di=dict(sorted(d.items(), key=lambda x: x[0], reverse=True))

print(f"Diem hoc sinh:")
for key,value in di.items():
    print(f"{key} : {value}")
