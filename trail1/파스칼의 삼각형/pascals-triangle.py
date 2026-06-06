n = int(input())
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(i + 1):
        if i == j or j == 0:
            arr_2d[i][j] = 1
        else:
            arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]

for i in range(n):
    for j in range(i + 1):
        print(arr_2d[i][j], end=" ")
    print()