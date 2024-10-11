day={1:"Sunday",
     2:"Monday",
     3:"Tuesday",
     4:"Wednesday",
     5:"Thursday",
     6:"Friday",
     7:"Saturday",}
while True:
    d=int(input("Nhap thu trong tuan = "))
    if (1<=d and d<=7):
        print(f"{day[d]}")
        break
    else:
        print("Hay nhao thu tu 1 den 7 !")
    