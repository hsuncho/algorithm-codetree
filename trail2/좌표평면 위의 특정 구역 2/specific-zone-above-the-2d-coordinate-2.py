n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = float('inf')

for i in range(n):
    xs = []
    ys = []
    for j in range(n):
        if j == i:
            continue
        
        xs.append(x[j])
        ys.append(y[j])
    
    area = (max(xs) - min(xs))*(max(ys) - min(ys))
    ans = min(ans, area)

print(ans)