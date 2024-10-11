s=input("Nhap chuoi = ")

alphabet={}
for i in s:
    if (i.isalpha()):
        if (i in alphabet):
            alphabet[i]+=1
        else:
            alphabet[i]=1
d={}           
d=dict(sorted(alphabet.items(), key=lambda x: x[0]))

for w,c in d.items():
    print(f"{w} : {c} lan")