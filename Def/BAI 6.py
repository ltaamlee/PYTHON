def DEC_TO_BIN(n):
    temp=int(n)
    res=''
    while (temp!=0):
        res=str(temp%2)+res
        temp//=2
    return res

def DEC_TO_HEX(n):
    temp=int(n)
    res=""
    hexa="0123456789ABCDEF"
    while (temp!=0):
        res=hexa[temp%16]+res
        temp//=16
    return res

def BIN_TO_DEC(n):
    temp=n
    res=0
    for i in range(len(temp)):
            res+=int(temp[i])*(2**(len(temp)-i-1))
    return res

def HEX_TO_DEC(n):
    res=0
    hexa="0123456789ABCDEF"
    temp=n.upper()
    for i in range(len(temp)):
        res+=hexa.index(temp[i].upper())*(16**(len(temp)-i-1))
    return res
    
def BIN_TO_HEX(n):
    d=BIN_TO_DEC(n)
    return DEC_TO_HEX(d)
    
def HEX_TO_BIN(n):
    d=HEX_TO_DEC(n)
    return DEC_TO_BIN(d)
    
while True:
    print("Chon he dem 2, 10, 16 : ")
    base=input()
    if (base=='2' or base=='10' or base=='16'):
        break
    else:
        print("Lua chon khong ton tai !")
        
while True:
    print("Chon he dem can chuyen 2, 10, 16 : ")
    convert=input()
    if (convert=='2' or convert=='10' or convert=='16'):
        break
    else:
        print("Lua chon khong ton tai !")
  
s=input("Nhap gia tri can chuyen : ")

if (base=='2'):
    if (convert=='10'):
        print(f"{s} (2) = {BIN_TO_DEC(s)} (10)")
    elif (convert=='16'):
        print(f"{s} (2) = {BIN_TO_HEX(s)} (16)")
elif (base=='10'):
    if (convert=='2'):
        print(f"{s} (10) = {DEC_TO_BIN(s)} (2)")
    elif (convert=='16'):
        print(f"{s} (10) = {DEC_TO_HEX(s)} (16)")
elif (base=='16'):
    if (convert=='2'):
        print(f"{s} (16) = {HEX_TO_BIN(s)} (2)")
    elif (convert=='10'):
        print(f"{s} (16) = {HEX_TO_DEC(s)} (10)")




