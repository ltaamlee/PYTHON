global cs
cs=4

def taxi(s):
    return(s/0.14)*0.25+cs

street=float(input("Nhap quang duong di chuyen (km): "))

print(f"Tien dich vu taxi : {taxi(street):.2f}")
