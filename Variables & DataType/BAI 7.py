import math
a,b,c=[float(a) for a in input().split()]
res=-b+math.sqrt(b*b-4*a*c)/(2*a)
print("{:.2f}".format(res))