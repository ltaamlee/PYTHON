def ROTATION_SPEED(r,m):
    l=[]
    for i in range(len(r)):
        if (r[i]<m):
            l.append([r[i],i])
    return l


n=int(input("Nhap so luong toc do quay cua dong co : "))
R=[]
for i in range(n):
    x=int(input())
    R.append(x)
    
Min=int(input("Nhap vap gia tri min cua dong co : "))

print(f"Cac toc do quay nho hon Min va chi so : {ROTATION_SPEED(R,Min)}")
