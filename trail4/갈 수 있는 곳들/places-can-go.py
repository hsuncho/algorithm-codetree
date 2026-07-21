from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
visited = [[False] * n for _ in range(n)]
q = deque()

for r, c in points:
    if grid[r-1][c-1] == 0 and visited[r-1][c-1] == False:
        visited[r-1][c-1] = True
        q.append((r-1, c-1))

cnt = len(q)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = dr[i] + r, dc[i] + c
        if 0 <= nr < n and 0 <= nc < n:
            if not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                cnt += 1
                q.append((nr, nc))
print(cnt)