N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

# Please write your code here.
ans = 0
for i in range(N):
    prices = []
    for j in range(N):
        
        p = P[j]
        s = S[j]

        if i == j:
            cost = p // 2 + s
        else:
            cost = p + s
        
        prices.append(cost)
    
    prices.sort()

    total = 0
    cnt = 0

    for price in prices:
        if total + price <= B:
            total += price
            cnt += 1
        else:
            break
    ans = max(ans, cnt)
print(ans)