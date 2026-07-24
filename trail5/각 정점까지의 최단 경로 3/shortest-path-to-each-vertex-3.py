import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = float('inf')
graph = [[] for _ in range(n)]
for u, v, w in edges:
    graph[u-1].append((v-1, w))

dist = [INF] * n
dist[0] = 0
pq = [(0,0)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]: 
        continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))
for v in range(1, n):
    print(dist[v] if dist[v] != INF else -1)