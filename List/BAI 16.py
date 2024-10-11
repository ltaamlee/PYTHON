import decimal
from decimal import Decimal
decimal.getcontext().prec=2

temperature=[]
for i in range(7):
    temperature.append(float(input(f"Nhap nhiet do ngay thu {i+1} = ")))

s=0
for i in temperature:
    s+=i
    
avg=s/7
cnt=0
for i in temperature:
    if (i>avg):
        cnt+=1
        
print(f"Nhiet do trung binh : {Decimal(avg)/Decimal(1)} °C")      
print(f"Co {cnt} ngay co nhiet do cao hon nhiet do trung binh")  