l=[int(i) for i in input("inputList = ").split(",")]

n=input("inputTuple = ")
tup=tuple(int(x) for x in n.split(","))

a=l+list(tup)
t=tuple(a)

print(a)
print(t)

