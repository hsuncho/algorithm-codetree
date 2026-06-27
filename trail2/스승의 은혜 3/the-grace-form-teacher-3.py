N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
prices = [P[k] + S[k] for k in range(N)]
ans = 0
for i in range(N):
    P[i] /= 2
    prices[i] = P[i] + S[i]
    prices.sort()
    
    total = 0
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        
        if total <= B:
            total += prices[j]
            cnt += 1
        ans = max(ans, cnt)
print(ans)