def FIND(s,x):
    cnt=0
    pos=s.find(x)
    while (pos!=-1):
        cnt+=1
        pos=s.find(x,pos+1)
        
    return cnt

s=input("Nhap chuoi : ")
x=input("Nhap chuoi con can tim : ")

print(f"Chuoi '{x}' xuat hien {FIND(s,x)} lan ")