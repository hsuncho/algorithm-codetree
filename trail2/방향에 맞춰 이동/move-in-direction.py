n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
x, y = 0, 0
dir_num = 0
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for i in range(n):
    if dir[i] == 'N':
        dir_num = 0
    elif dir[i] == 'S':
        dir_num = 1
    elif dir[i] == 'W':
        dir_num = 2
    elif dir[i] == 'E':
        dir_num = 3

    x += dx[dir_num] * dist[i]
    y += dy[dir_num] * dist[i]

print(x, y)