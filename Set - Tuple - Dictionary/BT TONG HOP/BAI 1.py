s=input("Nhap chuoi = ")

morse={"A":".-",
       "B":"-...",
       "C":"-.-.",
       "D":"-..",
       "E":".",
       "F":"..-.",
       "G":"--.",
       "H":"....",
       "I":"..",
       "J":".---",
       "K":"-.-",
       "L":".-..",
       "M":"--",
       "N":"-.",
       "O":"---",
       "P":".--.",
       "Q":"--.-",
       "R":".-.",
       "S":"...",
       "T":"-",
       "U":"..-",
       "V":"...-",
       "W":".--",
       "X":"-..-",
       "Y":"-.--",
       "Z":"--..",
       "0":"-----",
       "1":".----",
       "2":"..---",
       "3":"...--",
       "4":"....-",
       "5":".....",
       "6":"-....",
       "7":"--...",
       "8":"---..",
       "9":"----."}

s=s.upper()
print("Ma Morse: ")
for i in s:
    if (i in morse):
        print(f"{morse[i] }",end=" ")
    else:
        continue
