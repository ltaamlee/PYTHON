active={"hoc":720,
        "an":120,
        "ngu":150,
        "choi":100}
#a
a=input("Nhap them hoat dong : ")
a=a.lower()
m=int(input("Nhap so phut cua hoat dong : "))
if a in active:
    active[a]+=m
else:
    active[a]=m
#2
for key,value in active.items():
    h=value/60
    print(f"{key:<6} : {h:.1f} gio")
#3
d=sorted(active.items(), key=lambda x: x[1], reverse=True)
max_2=d[:2]
print("Hai hoat dong co thoi gian nhieu nhat: ")
for key,value in max_2:
    print(f"{key:<6} : {value}")
    
min_2=d[-2:]
print("Hai hoat dong co thoi gian it nhat:")
for key,value in min_2:
    print(f"{key:<6} : {value}")