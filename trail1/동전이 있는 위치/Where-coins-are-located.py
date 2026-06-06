n, m = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end = " ")
    print()