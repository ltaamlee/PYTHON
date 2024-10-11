a=[]
while True:
    n=int(input("Nhap n = "))
    if (n>=0):
        for i in range(n):
            a.append(int(input(f"a[{i+1}] = ")))
        
        print("Danh sach cac so chan:",end=" ")
        for i in a: 
            if (i%2==0):
                print(i,end=" ")
        print()        
        print("Danh sach cac so le:",end=" ")
        for i in a: 
            if (i%2!=0):
                print(i,end=" ")           
        break     
    else:
        print("Hay nhap n >= 0 !")        
            