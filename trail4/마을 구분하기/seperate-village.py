n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
cnt = 0

def dfs(x, y):
    count = 1
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < n and 0 <= ny < n):
            continue
        
        if grid[nx][ny] == 0:
            continue

        if visited[nx][ny]:
            continue
        
        count += dfs(nx, ny)
    return count
        
village_size = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            village_size.append(dfs(i, j))

print(len(village_size))
village_size.sort()
for s in village_size:
    print(s)