def check(s):
    h=0
    t=0
    m=0
    if len(s)>=8:
        for i in s:
            if i.isalpha():
                if i.isupper():
                    h+=1
                elif i.lower():
                    t+=1
            elif i.isdigit():
                m+=1
        if (h>=1 and t>=1 and m>=1):
            return True
        else:
            return False
    else:
        return False

password=input("Nhap vao mat khau : ")
if (check(password)):
    print("Mat khau co tinh bao mat cao !")
else:
    print("Mat khau co tinh bao mat thap !")