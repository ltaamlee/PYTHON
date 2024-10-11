it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
print(f"1. Chieu dai tap hop it_companies = {len(it_companies)}\n")
#2
it_companies.add("Twitter")
print(f"2. {it_companies}\n")

#3
it_companies.update({"Bing","LinkedIn"})
print(f"3. {it_companies}\n")
#4
it_companies.remove("Google")
print(f"4. {it_companies}\n")
#5
#6
C=A.union(B) #A|B
print(f"6. A|B = {C}\n")
#7
D=A.intersection(B) #A&B
print(f"7. A&B = {D}\n")
#10
E=A.union(B)
F=B.union(A)
print(f"10. A|B = {E}\n B|A = {F}\n")
#11
G=A.symmetric_difference(B) #A^B
print(f"11. A-B = {G}\n")
#12
A.clear()
B.clear()
print(f"12. Set A va B sau khi xoa: {A} {B}\n")
#13
s=set(age)
print(f"13. Len set = {len(s)} ; Len age = {len(age)}")
