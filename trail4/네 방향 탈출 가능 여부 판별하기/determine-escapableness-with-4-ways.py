from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0)])
visited[0][0] = True

while q:
    x, y = q.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and a[nx][ny] == 1:
            visited[nx][ny] = True
            q.append((nx, ny))

print(1 if visited[n - 1][m - 1] else 0)