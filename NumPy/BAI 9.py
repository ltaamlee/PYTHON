import numpy as np

def broadcast(vec,n):
    res=np.tile(vec,(n,1)).T
    return res

vec=np.array(list(map(int,input("Nhap vector, cac so cach nhau khoang trang : ").split())))
n=int(input("Nhap so cot : "))
print(f"Ma tran sau khi broadcast : \n{broadcast(vec,n)}")