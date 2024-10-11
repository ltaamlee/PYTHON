def FIND(s):
    l= []
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            if s[i:j] not in l:
                l.append(s[i:j])
    return l

s=input("Nhap chuoi : ")
l=FIND(s)
print("Cac xau con cua chuoi : ",end="")
for i in l:
    print(i)
