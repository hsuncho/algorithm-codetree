from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
r, c = r-1, c-1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(k):
    x = grid[r][c]
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    q = deque([(r, c)])
    best_val, best_r, best_c = -1, -1, -1
    
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] < x:
                visited[nr][nc] = True
                q.append((nr, nc))
                v = grid[nr][nc]
                if v > best_val or (v == best_val and (nr < best_r or (nr == best_r and nc < best_c))):
                    best_val, best_r, best_c = v, nr, nc

    if best_val == -1:
        break
    r, c = best_r, best_c
print(r+1, c+1)