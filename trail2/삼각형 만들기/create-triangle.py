n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = 0
for i in range(n): # 기준점
    for j in range(n): # 가로변
        for k in range(n): # 세로변
            if i == j or j == k or k == i:
                continue
            
            if y[i] == y[j] and x[i] == x[k]:
                area = abs(x[i] - x[j]) * abs(y[i] - y[k])
                ans = max(area, ans)
print(ans)