from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([(r1, c1)])
    dist[r1][c1] = 0
    
    while q:
        r, c = q.popleft()
        if r == r2 and c == c2:
            return dist[r][c]
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return -1
print(bfs())