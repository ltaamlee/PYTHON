def NegativeNumberInStrings(s):
    x=""
    res=[]
    for i in s:
        if (i=="-"):
            x=i
        elif (i.isdigit()):
            x+=i
        else:
            if (len(x)>1):
                res.append(x)
                x=""
    if (len(res)==0):
        print("Chuoi khong co so am !")
    else:
        for c in res:
            print(c,end=" ")
            
s=input("Nhap chuoi : ")
NegativeNumberInStrings(s)
            