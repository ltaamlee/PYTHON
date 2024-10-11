n=int(input("Nhap so nguyen duong N = "))
temp=n
odd=0
even=0
r=0
while(temp!=0):
    r=temp%10
    if (r%2==0):
        even+=1
    else:
        odd+=1
    temp//=10
print(f"{n} co {even} chu so chan, {odd} chu so le")
