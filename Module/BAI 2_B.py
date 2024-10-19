from random_num import gen_num

n=int(input("Nhap so luong phan tu : "))
Min=int(input("Nhap gia tri Min : "))
Max=int(input("Nhap gia tri Max : "))

res=gen_num(n,Min,Max)
print(f"Day so ngau nhien trong khoang [{Min}..{Max}] : ",res)
