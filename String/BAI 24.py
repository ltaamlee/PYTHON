def COUNT(s):
    s=s.lower()
    d={}
    x=s.split()
    for i in x:
        i=i.strip(".,?!()-#;:'\"[]+_&*^%$@`~<>/")
        if i.isalpha():
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    return d

s=input("Nhap chuoi : ")
dic=COUNT(s)
for key,val in dic.items():
    print(f"Tu {key} xuat hien {val} lan")