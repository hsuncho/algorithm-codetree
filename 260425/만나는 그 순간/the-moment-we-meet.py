n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

pos_a = [0]
pos_b = [0]

for i in range(n):
    for _ in range(t[i]):
        if d[i] == 'R':
            pos_a.append(pos_a[-1] + 1)
        else:
            pos_a.append(pos_a[-1] - 1)

for i in range(m):
    for _ in range(t2[i]):
        if d2[i] == 'R':
            pos_b.append(pos_b[-1] + 1)
        else:
            pos_b.append(pos_b[-1] - 1)

answer = -1

for i in range(1, min(len(pos_a), len(pos_b))):
    if pos_a[i] == pos_b[i]:
        answer = i
        break

print(answer)