n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * n for _ in range(n)] # 최대 합
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[0][0] = grid[0][0]

        elif i == 0:
            dp[i][j] = dp[i][j-1] + grid[i][j]

        elif j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
print(dp[n-1][n-1])