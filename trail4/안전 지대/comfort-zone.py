import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def dfs(x, y, k):
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > k:
            dfs(nx, ny, k)
max_height = max(max(row) for row in grid)

best_k, best_cnt = 1, 0
for k in range(1, max_height + 1):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                cnt += 1
    if cnt > best_cnt :
        best_cnt = cnt
        best_k = k
print(best_k, best_cnt)