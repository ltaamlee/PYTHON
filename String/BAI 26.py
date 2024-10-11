import random

def RANDOM():
    plen=random.randint(8,20)
    p=[ random.randint(65,90),
        random.randint(97,122),
        random.randint(48,57),
        random.randint(33,47)
        ]
    while (len(p) < plen):
        choice=random.randint(1,4)
        if (choice==1):
            p.append(random.randint(65,90))
        elif (choice==2):
            p.append(random.randint(97,122))
        elif (choice==3):
            p.append(random.randint(48,57))
        else:
            p.append(random.randint(33,47))
            
    return p

def TRANS(p):
    res=""
    for i in p:
        res+=chr(i)
    return res

s=RANDOM()
print(f"Password ngau nhien : {TRANS(s)}")
    