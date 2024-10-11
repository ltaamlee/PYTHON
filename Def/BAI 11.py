def PT_BAC2(a,b,c):
    l=[]
    if (a==0):
        if (b==0):
            if (c==0):
                l.append('Phuong trinh vo so nghiem')
            else:
                l=[]
        else:
            l.append(round((-c/b),2))
    else:
        delta=b*b-4*a*c
        if delta<0:
            l=[]
        elif delta==0:
            l.append(round(-b/(2*a),2))
        else:
            l.append(round((-b+sqrt(delta))/(2*a),2))
            l.append(round((-b-sqrt(delta))/(2*a),2))
    return l

from math import sqrt
A=int(input())
B=int(input())
C=int(input())
print(PT_BAC2(A,B,C))