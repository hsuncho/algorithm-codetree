n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0
for i in range(m): # i = 열 변호
    if i % 2 == 0:
        for j in range(n): # j = 행 반호
                arr_2d[j][i] = num
                num += 1
    else:
        for j in range(n -1, -1, -1):
            arr_2d[j][i] = num
            num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()