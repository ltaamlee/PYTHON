def COUNT(s):
    num=0
    h=0
    t=0
    sp=0
    for i in s:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            if i.isupper():
                h+=1
            elif i.islower():
                t+=1
        else:
            sp+=1
    return num,h,t,sp

s=input("Nhap chuoi : ")
n,h,t,sp=COUNT(s)
print(f"Co {n} ki tu so\nCo {h} ki tu chu in hoa\nCo {t} ki tu chu in thuong\nCo {sp} ki tu dac biet")