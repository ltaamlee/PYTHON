import numpy as np

a=int(input("Nhap a = "))
b=int(input("Nhap b = "))

arr=a+(b-a)*np.random.randn(10)

print(f"Cac so thuc trong khoang tu {a} den {b} : \n {arr}")
