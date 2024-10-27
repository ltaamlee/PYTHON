import numpy as np

def product(mat_a, mat_b):
    try:
        mult=np.dot(mat_a,mat_b)
        print("Tich 2 ma tran : \n",mult)
    except ValueError:
        print("Khong co tich ma tran !")
    try:
        if (mat_a.shape==mat_b.shape):
            hada=np.multiply(mat_a,mat_b)
            print("Tich Hadamard cua 2 ma tran : \n",hada)
        else:
            print("Khong co tich Hadamard !")
    except ValueError:
        print("Khong co tich Hadamard !")
        
rA=int(input("Nhap so dong cua ma tran A : "))
cA=int(input("Nhap so cot cua ma tran A : "))
mat_a=np.array(list(map(int,input("Nhap ma tran A, cac so cach nhau khoang trang : ").split())))
mat_a=mat_a.reshape(rA,cA)
print("Ma tran A: \n",mat_a)
print()
rB=int(input("Nhap so dong cua ma tran B : "))
cB=int(input("Nhap so cot cua ma tran B : "))
mat_b=np.array(list(map(int,input("Nhap ma tran B, cac so cach nhau khoang trang : ").split())))
mat_b=mat_b.reshape(rB,cB)
print("Ma tran B: \n",mat_b)
print()
product(mat_a,mat_b)