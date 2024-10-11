def XCDN(s):
    res=""
    d={}
    lenmax=0
    l=0
    start=0
    for index, char in enumerate(s):
        if (char in d and d[char] >= start):
            start=d[char]+1
        else:
            l=index-start+1
            if (l>lenmax):
                lenmax=l
                res=s[start:index+1]
        d[char]=index
        
    return res

s=input("Nhap chuoi : ")
print(XCDN(s))