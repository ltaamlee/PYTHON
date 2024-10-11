def isPalindrome(s1, s2):
    if (s1==s2[::-1]):
        return "S1 la xau dao nguoc cua S2"
    return "S1 khong la xau dao nguoc cua S2"

s1=input("Nhap chuoi S1 : ")
s2=input("Nhap chuoi S2 : ")
print(isPalindrome(s1,s2))