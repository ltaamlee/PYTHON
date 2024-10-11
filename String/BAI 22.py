def TrueID(s):
    if (len(s))!=12:
        return False
    for i in s:
        if not i.isdigit():
            return False
    return True

def CCCD(s):
    tinh=s[:3]
    gt=s[3]
    nam=s[4:6]
    dinhdanh=s[6:]
    return f"Ma tinh : {tinh}\nGioi tinh : {'Nam' if gt=='2' or gt=='0' else 'Nu'}\nNam sinh : {('19' + nam) if gt=='0' or gt=='1' else ('20'+nam)}\nDinh danh : {dinhdanh}"


s=input("Nhap chuoi so CCCD : ")
if (TrueID(s)):
    print("So CCCD hop le !")
    print(CCCD(s))
else:
    print("So CCCD khong hop le !")