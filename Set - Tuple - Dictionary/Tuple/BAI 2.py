tup=()
a=[]
while True:
    n=input()
    if n!="":
        name,age,score=n.split(",")
        age=int(age);
        score=float(score)
        tup+=(name,age,score)
        a.append(tuple(name,age,score))
    else:
        break
'''tup=sorted(tup,key=lambda u:(u[0],u[1],u[2]))'''

a.sort()
print(a)