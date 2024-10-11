while True:
    n=int(input("Nhap n = "))
    if (n>=0): 
        a=[x for x in range (n+1)]
        print(a)
        b=[x**2 for x in range (n)]
        print(b)
        break
    else:
        print("Hay nhap n>=0 !")
