n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 1
max_cnt = 1

for i in range(1, n):
    if arr[i] > arr[i-1] and arr[i-1] > t:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)