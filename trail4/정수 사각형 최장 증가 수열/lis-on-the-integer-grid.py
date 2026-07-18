n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[1] * n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cells = []
for r in range(n):
    for c in range(n):
        cells.append((grid[r][c], r, c))
cells.sort(reverse = True)

for _, r, c in cells:
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] > grid[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dp[nr][nc])
print(max(map(max, dp)))