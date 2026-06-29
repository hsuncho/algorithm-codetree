n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[min_idx] > arr[j]:
            arr[j], arr[min_idx] = arr[min_idx], arr[j]
for a in arr:
    print(a, end = " ")