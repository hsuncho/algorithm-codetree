N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.
idx = P.index(max(P))
ans = 0
for i in range(N):
    prices = P[:]
    prices[i] //= 2
    prices.sort()
    
    total = 0
    cnt = 0
    for p in prices:
        if total + p <= B:
            total += p
            cnt += 1
        else:
            break
    ans = max(ans, cnt)
print(ans)