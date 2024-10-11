def AVG(x):
    s=0
    cnt=0
    while x>0:
        s+=x%10
        x//=10
        cnt+=1
    return s/cnt
n=int(input())
print("{:.2f}".format(AVG(n)))