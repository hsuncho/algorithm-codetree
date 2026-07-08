n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)

vertex_cnt = 0
def dfs(vertex):
    global vertex_cnt
    for nxt in graph[vertex]:
        if not visited[nxt]:
            visited[nxt] = True
            vertex_cnt += 1
            dfs(nxt)
visited[1] = True
dfs(1)
print(vertex_cnt)