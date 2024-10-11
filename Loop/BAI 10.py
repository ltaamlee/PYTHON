def SUM(x):
    ss=0
    temp=x
    while(temp!=0):
        ss+=temp%10
        temp//=10
    return ss
s=0
while True:
    n=int(input("Nhap n = "))
    if (n>0):
        s=SUM(n)
        break
    else:
        print("Hay nhap n > 0 !")
print("S =",s)