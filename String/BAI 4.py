def palindrome(s):
    if (s==s[::-1]):
        return "Chuoi doi xung !"
    return "Chuoi khong doi xung !"

s=input("Nhap chuoi : ")
print(palindrome(s))