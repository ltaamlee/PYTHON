while True:
    lt=int(input("Nhap diem ly thuyet = "))
    if (0<=lt and lt<=10):
        break
    else:
        print("Nhap diem trong khoang [0..10]")

while True:
    th=int(input("Nhap diem thuc hanh = "))
    if (0<=th and th<=10):
        break
    else:
        print("Nhap diem trong khoang [0..10]")
avg=(lt+th)/2
print("Trung binh cong = {:.2f}".format(avg))