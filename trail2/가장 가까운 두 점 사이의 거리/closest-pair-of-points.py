n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        diff1 = x[i] - x[j]
        diff2 = y[i] - y[j]
        ans = min(ans, diff1**2 + diff2**2)
print(ans)