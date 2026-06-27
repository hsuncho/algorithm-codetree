n = int(input())
l = []
r = []
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)

# Please write your code here.
ans = 0
for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
        
            crossed = False
            for i in range(n):
                if i == a or i == b or i == c:
                    continue
            
                for j in range(i+1, n):
                    if j == a or j == b or j == c:
                        continue

                    if not(r[i] < l[j] or r[j] < l[i]):
                        crossed = True
                        break
            if not crossed:
                ans += 1
print(ans)