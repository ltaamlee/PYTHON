s=input("Nhap chuoi: ")
num=0
char=0
for i in s:
    if (i.isalpha()):
        char+=1
    if (i.isdigit()):
        num+=1

print(f"So ky tu chu: {char}, so ky tu la so: {num}")
        