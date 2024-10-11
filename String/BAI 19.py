def ASCII(s):
    res=" " 
    for i in s:
        res+=(str(ord(i)))+" "
    return res.strip()

def toString(asc):
    res=""
    x=asc.split(" ")
    for i in x:
        res+=chr(int(i))
    return res
        
s=input("Nhap chuoi : ")
print(f"Chuoi sau khi chuyen sang ma ASCII : {ASCII(s)}")

s=input("Nhap chuoi ASCII : ")
print(f"Chuoi sau khi chuyen tu ma ASCII : {toString(s)}")