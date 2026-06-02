n = int(input())

arr_2d = [
    [ 0 for _ in range(n) ]
    for _ in range(n)
]

num = 1
for c in range(n - 1, -1, -1):
    if c % 2 == 1:
        for r in range(n - 1, -1, -1):
            arr_2d[r][c] = num
            num += 1
    else:
        for r in range(n):
            arr_2d[r][c] = num
            num += 1

for r in range(n):
    for c in range(n):
        print(arr_2d[r][c], end = " ")
    print() 