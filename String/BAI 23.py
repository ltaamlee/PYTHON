def CHECK(s):
    if '@' not in s:
        return False
    e=s.split('@')
    if (len(e)!=2):
        return False
    m=e[1]
    if '.' not in m:
        return False
    return True


s=input("Nhap dia chi thu dien tu : ")
if CHECK(s):
    print("Dia chi hop le !")
else:
    print("Dia chi khong hop le !")