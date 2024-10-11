max_x=float("-inf")
while True:
    n=int(input("Nhap n = "))
    if (n>0):
        for i in range (1,n+1):
            x=int(input())
            if (x>max_x and x%2!=0):
                max_x=x
        print("So le lon nhat trong cac so = ",max_x)
        print("Nguoi dung co muon tiep tuc khong?")
        print("Neu co nhan 'c', neu khong nhan bat kki ki tu tren ban phim")
        sym=input()
        if (sym!='c'):
            break
    else:
        print("Hay nhap n > 0 !")