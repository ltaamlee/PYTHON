neg=0
while True:
    n=int(input())
    if (n<0):
        neg+=1
    elif (n==0):
        break
print(f"Co {neg} so am")
