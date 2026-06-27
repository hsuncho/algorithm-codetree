k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
rank = [[0] * (n + 1) for _ in range(k)]

for i in range(k):
    for pos in range(n):
        dev = arr[i][pos]
        rank[i][dev] = pos

ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            continue
        always_higher = True

        for game in range(k):
            if rank[game][a] > rank[game][b]:
                always_higher = False
        
        if always_higher:
            ans += 1
print(ans)