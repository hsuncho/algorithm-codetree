n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for r in range(n-2):
    for c in range(n-2):
        box = [row[c:c+3] for row in grid[r:r+3]]
        cnt = sum(num for b in box for num in b)
        answer = max(answer, cnt)
print(answer)
