N = int(input())
dp = [2, 4, 7]
res = [0 for _ in range(3, N)]
dp.extend(res)

for i in range(3, N):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

print(dp[N-1])