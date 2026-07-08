from collections import deque
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1

    # 인접 리스트 (양방향)
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        graph[u].append(v)
        graph[v].append(u)   # 양방향이므로 양쪽 모두 추가

    visited = [False] * (N + 1)
    visited[1] = True
    queue = deque([1])
    count = 0  

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                count += 1      
                queue.append(nxt)

    print(count)

solve()