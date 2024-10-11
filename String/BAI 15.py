def FIND(s,n):
    l=[]
    d=len(s)
    for i in range(d):
        for j in range(i+n,d+1):
            l.append(s[i:j])
    return l

s=input("Nhap chuoi : ")
n=int(input("Nhap do dai toi thieu cua xau con : "))
res=FIND(s,n)
print(f"Cac xau con co do dai toi thieu {n} : ")
for str in res:
    print(str)