row = 2
col = 4

arr_2d = [
    list(map(int, input().split())) for _ in range(row)
]

for r in range(row):
    avg = sum(arr_2d[r]) / col
    print(f"{avg:.1f}", end = ' ')
print()

for c in range(col):
    total = 0
    for r in range(row):
        total += arr_2d[r][c]
    avg = total / row
    print(f"{avg:.1f}", end = ' ')

print()

total = 0
for r in range(row):
    for c in range(col):
        total += arr_2d[r][c]

avg = total / (row *col)
print(f"{avg:.1f}")
