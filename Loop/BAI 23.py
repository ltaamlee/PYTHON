def BIN_TO_DEC(s):
    dec=0
    for i in range(len(s)):
        if (s[i]=='1'):
            dec+=2**((len(s)-i)-1)
    return dec

s=input("Nhap so he nhi phan = ")
print(f"{s} (2) = {BIN_TO_DEC(s)} (10)")