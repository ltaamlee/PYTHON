import numpy as np
a=np.random.randint(0,101, size=(2,7))
print(f"So luong hang hoa ban ra cua cua hang :\n{a}")

max_day=np.argmax(a.sum(axis=0))

print(f"Ngay ban duoc nhieu nhat tuan: Ngay thu {max_day+1}")
    
max_sale=0
time=(0,0)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i,j]>max_sale:
            max_sale=a[i,j]
            time=(i,j)
            
print(f"Thoi diem ban duoc nhieu nhat : buoi {'sang' if time[0]=='0' else 'chieu'}, ngay {time[1]+1}")

sang=0
chieu=0
for i in range(a.shape[1]):
    if (a[0,i] > a[1,i]):
        sang+=1
    elif (a[0,i] < a[1,i]):
        chieu+=1

if (sang>chieu and sang>=4):
    print("Buoi sang co khuynh huong ban hang duoc nhieu hon ")
elif (sang<chieu and chieu>=4):
    print("Buoi chieu co khuynh huong ban hang duoc nhieu hon")
else:
    print("Khuynh huong ban duoc hang cua hai buoi la nhu nhau")