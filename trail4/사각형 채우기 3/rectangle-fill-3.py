n = int(input())

# Please write your code here.
MOD = 1000000007
dp = [0] * (n + 1)
gap = [0] * (n + 1)
dp[0] = 1
if n >= 1:
    dp[1] = 2
    gap[1] = 1
for i in range(2, n+1):
    gap[i] = (dp[i-1] + gap[i-1]) % MOD

    dp[i] = (2 * dp[i-1] + 2 * gap[i-1] + dp[i-2]) % MOD

print(dp[n])