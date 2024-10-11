def COUNT(s):
    d={}
    s=s.lower()
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    Max=max(d.values())
    res=[i for i, v in d.items() if v==Max]
    
    return res
        

s=input("Nhap chuoi : ")
print("Ki tu xuat hien nhieu nhat : ",COUNT(s))