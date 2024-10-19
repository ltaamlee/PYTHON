from math import sqrt

def PT_BAC2(a,b,c):
    l=[]
    if (a==0):
        if (b==0):
            if (c==0):
                l.append('Phuong trinh vo so nghiem')
            else:
                l.append('Phuong trinh vo nghiem')
        else:
            l.append(round((-c/b),2))
    else:
        delta=b*b-4*a*c
        if delta<0:
            l.append('Phuong trinh vo nghiem')
        elif delta==0:
            l.append(round(-b/(2*a),2))
        else:
            l.append(round((-b+sqrt(delta))/(2*a),2))
            l.append(round((-b-sqrt(delta))/(2*a),2))
    return l