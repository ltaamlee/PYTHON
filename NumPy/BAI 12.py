import numpy as np

def replace_col(mat, col_ind):
    mat[:,col_ind]=1
    return mat

r=int(input("Nhap so dong cua ma tran : "))
c=int(input("Nhap so cot cua ma tran : "))

mat=np.array(list(map(int,input("Nhap ma tran cac so cach nhau khoang trang : ").split())))
mat=mat.reshape(r,c)
print("Ma tran vua nhap : \n",mat)
col_ind=int(input("Nhap cot muon thay doi : "))
print(f"Ma tran sau khi thay doi gia tri cua cot {col_ind} : \n{replace_col(mat,col_ind)}")