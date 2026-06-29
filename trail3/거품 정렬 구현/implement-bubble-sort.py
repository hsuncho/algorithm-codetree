n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
for a in arr:
    print(a, end=" ")