n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

pos_a = [0]
pos_b = [0]

for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'R':
            pos_a.append(pos_a[-1] + 1)
        elif d[i] == 'L':
            pos_a.append(pos_a[-1] - 1)

for i in range(m):
    for _ in range(t_b[i]):
        if d_b[i] == 'R':
            pos_b.append(pos_b[-1] + 1)
        elif d_b[i] == 'L':
            pos_b.append(pos_b[-1] - 1)

max_len = max(len(pos_a), len(pos_b))
while len(pos_a) < max_len:
    pos_a.append(pos_a[-1])

while len(pos_b) < max_len:
    pos_b.append(pos_b[-1])

cnt = 0
for i in range(1, max(len(pos_a), len(pos_b))):
    if pos_a[i] == pos_b[i] and pos_a[i-1] != pos_b[i-1]:
        cnt += 1

print(cnt)