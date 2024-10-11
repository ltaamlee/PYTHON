def COUNT(s):
    cnt=0
    for i in s:
        if (i=="1"):
            cnt+=1
    return cnt
while True:
    bit=input("Nhap chuoi nhi phan : ")
    if (bit!=" "):
        if (len(bit)>8):
            print("Hay nhap chuoi co do dai khong qua 8 bit !")
            continue
        print("Parity chan(c) hay le(l)? :")
        c=input()
        if (c=="c"):
            if (COUNT(bit)%2==0):
                parity="0"
            else:
                parity="1"
        elif (c=="l"):
            if (COUNT(bit)%2==0):
                parity="1"
            else:
                parity="0"
                
        print(f"Bit Parity = {parity}")
    else:
        break
            
    
    
    
