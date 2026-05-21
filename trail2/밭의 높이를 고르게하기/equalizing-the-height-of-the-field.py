N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

min_val = 10000

for i in range(N-T+1):
    val = 0

    for j in range(i, i+T):
        val += abs(H-arr[j])
    min_val = min(val, min_val)

print(min_val)