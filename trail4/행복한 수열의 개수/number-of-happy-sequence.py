n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0
col_seq = [[grid[row][col] for row in range(n)] for col in range(n)]

def is_happy(seq, m):
    cnt = 1
    if m == 1:
        return True
    for i in range(1, len(seq)):
        if seq[i-1] == seq[i]:
            cnt += 1
            if cnt >= m:
                return True
        else:
            cnt = 1
    return False

for row in grid:
    if is_happy(row, m):
        answer += 1

for col in col_seq:
    if is_happy(col, m):
        answer += 1

print(answer)

