def symmetrical(s):
    mid=len(s)//2
    l=s[:mid]
    
    if (len(s)%2==0):
        r=s[mid:]
    else:
        r=s[mid+1:]

    if (l==r):
        return "La chuoi symmetrical"
    return "Khong la symmetrical"
        
s=input("Nhap chuoi : ")
print(symmetrical(s))