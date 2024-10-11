n=int(input("Nhap n = "))
s=[int(i) for i in input("Nhap tap cac dong xu = ").split(",")]

dp=[0]*(n+1)
dp[0]=1
for num in s:
    for i in range(num,n+1):
        dp[i]+=dp[i-num]
print(f"Co {dp[n]} cach doi tien");