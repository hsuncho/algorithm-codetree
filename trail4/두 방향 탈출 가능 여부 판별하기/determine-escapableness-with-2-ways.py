n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]
trace = 0
dxs, dys = [0, 1], [1, 0]
x, y = 0, 0
def dfs(x, y):
    global trace
    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = x + dx, y + dy

        if not (0 <= nxt_x < n and 0 <= nxt_y < m):
            continue
        
        if grid[nxt_x][nxt_y] != 1:
            continue

        if nxt_x == n-1 and nxt_y == m-1:
            trace = 1
            break

        if not visited[nxt_x][nxt_y]:
            visited[nxt_x][nxt_y] = True
            dfs(nxt_x,nxt_y)

visited[0][0] = True
dfs(0, 0)
print(trace)