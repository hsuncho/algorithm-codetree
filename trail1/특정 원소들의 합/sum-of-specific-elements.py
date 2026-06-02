row, col = 4, 4
arr_2d = [
    list(map(int, input().split()))
    for _ in range(row)
]

total = 0
for r in range(row):
    for c in range(r + 1):
        total += arr_2d[r][c]
print(total)