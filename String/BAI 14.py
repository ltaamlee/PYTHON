def CHANGE(s,o,n):
    res=s.replace(o,n)
    return res

s=input("Nhap chuoi : ")
o=input("Nhap ki tu can thay doi : ")
n=input("Nhap ki tu can thay the : ")
print(f"Chuoi sau khi thay the ki tu : {CHANGE(s,o,n)}")