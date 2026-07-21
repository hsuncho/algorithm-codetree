from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
starts = list(zip(r, c))
stones = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(removed):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for (sr, sc) in starts:
        if (grid[sr][sc] == 0 or (sr, sc) in removed) and not visited[sr][sc]:
            visited[sr][sc] = True
            q.append((sr, sc))
    cnt = len(q)

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] == 0 or (nr, nc) in removed:
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr, nc))
    return cnt
answer = 0
for removed in combinations(stones, m):
    answer = max(answer, bfs(set(removed)))
print(answer)