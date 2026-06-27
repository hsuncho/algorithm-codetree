N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
ans = -1
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if num[i] == num[j] and abs(i - j) <= K:
            ans = max(num[i], ans)
print(ans)