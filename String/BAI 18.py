def FIND(s):
    x=set()
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            xc=s[i:j]
            if s.count(xc)>1:
                x.add(xc)
    
    res=sorted(x,key=len)
    return res

s=input("Nhap chuoi : ")
res=FIND(s)
print("Cac xau con lap lai : ")
for i in res:
    print(i)
        