x=int(input("Nhap x = "))
guess=x/2.0
while (abs(guess*guess-x)>1e-12):
    guess=(guess+x/guess)/2.0
print(guess)