def COUNT(x):
    cnt=0
    temp=x
    while(temp!=0):
        r=temp%10
        if (r==7):
            cnt+=1
        temp//=10
    return cnt
cnt=0
while True:
    n=int(input("Nhap n = "))
    if (n>0):
        cnt=COUNT(n)
        break
    else:
        print("Hay nhap n > 0 !")
print(f"Co {cnt} so 7")
