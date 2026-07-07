n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
## ab
## cd
answer = 0
for row in range(n-1):
    for col in range(m-1):
        acd = grid[row][col] + grid[row+1][col] + grid[row+1][col+1]
        bcd = grid[row][col+1] + grid[row+1][col] + grid[row+1][col+1]
        abc = grid[row][col] + grid[row][col+1] + grid[row+1][col]
        abd = grid[row][col] + grid[row][col+1] + grid[row+1][col+1]
        val = max(acd, bcd, abc, abd)
        answer = max(val, answer)
for row in range(n):
    for col in range(m-2):
        val = grid[row][col] + grid[row][col+1] + grid[row][col+2]
        answer = max(answer, val)

for row in range(n-2):
    for col in range(m):
        val = grid[row][col] + grid[row+1][col] + grid[row+2][col]
        answer = max(answer ,val)

print(answer)