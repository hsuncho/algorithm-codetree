n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt = 0
for i in range(n):
    x1, x2 = lines[i]
    crossed = False
    for j in range(n):
        if i == j:
            continue
        x3, x4 = lines[j]
        if (x1 < x3 and x2 > x4) or (x1 > x3 and x2 < x4):
            crossed = True
    
    if not crossed:
        cnt += 1
                
print(cnt)