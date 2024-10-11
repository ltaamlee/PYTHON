def CHECK(s):
    num=0
    al=0
    sp=0
    if (len(s)<8):
        return "Password yeu !"
    for i in s:
        if i.isdigit():
            num+=1
        if i.isalpha():
            al+=1
        else:
            sp+=1
    if num==0 or al==0 or sp==0:
        return "Password yeu !"
    return "Password manh !"

s=input("Nhap password : ")
print(CHECK(s))