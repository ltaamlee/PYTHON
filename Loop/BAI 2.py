from math import sqrt
from math import trunc
n=int(input("Nhap n = "))
if (sqrt(n)==trunc(sqrt(n))):
    print("Yes")
else:
    low=int(sqrt(n))**2
    high=(int(sqrt(n))+1)**2
    if (n-low<=high-n):
        print(low)
    else:
        print(high)