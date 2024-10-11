def XCDN(s):
    if len(s) == 0:
        return ""
    unique = set(s)
    lenmax=0
    res=""
    left=0
    count= {}

    for right in range(len(s)):
        count[s[right]]=count.get(s[right],0)+1
        while len(count)==len(unique):
            if (right - left + 1) > lenmax:
                lenmax= right-left+1
                res=s[left:right+1]
            count[s[left]]-=1
            
            if (count[s[left]]==0):
                del count[s[left]]
            left+=1
            
    return res

s=input("Nhap chuoi : ")
print("Xau con dai nhat chua tat cac cac ki tu :",XCDN(s))