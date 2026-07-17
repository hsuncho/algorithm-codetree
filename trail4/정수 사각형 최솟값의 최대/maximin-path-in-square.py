n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * n for _ in range(n)]

for i in range(n):
    min_val = 100
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]

        elif i == 0:
            dp[i][j] = min(dp[i][j-1], grid[i][j])
        
        elif j == 0:
            dp[i][j] = min(dp[i-1][j], grid[i][j])

        else:
            dp[i][j] = max(min(dp[i][j-1], grid[i][j]),
                            min(dp[i-1][j], grid[i][j]))
print(dp[n-1][n-1])