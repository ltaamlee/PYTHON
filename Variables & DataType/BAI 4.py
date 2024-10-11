def NUM(x):
    s=0
    while x>0:
        s+=x%10
        x//=10
    if s>10:
        s%=10
    return s
n=int(input())
print(NUM(n))
