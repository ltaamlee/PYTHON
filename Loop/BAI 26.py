def DEC_TO_BIN(n):
    bina=""
    while (n!=0):
        if (n%2==0):
            bina="0"+bina
        else:
            bina="1"+bina
        n//=2
    return bina

n=int(input("Nhap so he thap phan = "))
print(f"{n} (10) = {DEC_TO_BIN(n)} (2)")