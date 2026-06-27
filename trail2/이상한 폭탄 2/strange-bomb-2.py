N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        if num[i] == num[j] and abs(i - j) <= K:
            cnt = num[i]
    
    ans = max(cnt, ans)
print(ans)