n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
max_sum = 0
for i in range(n-k+1):
    total = sum(arr[i:i+k])
    max_sum = max(max_sum, total)

print(max_sum)