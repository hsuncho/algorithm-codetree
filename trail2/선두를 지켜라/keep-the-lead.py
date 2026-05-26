n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

pos_a = [0]
pos_b = [0]

for i in range(n):
    for _ in range(t[i]):
        pos_a.append(pos_a[-1] + v[i])
    
for i in range(m):
    for _ in range(t2[i]):
        pos_b.append(pos_b[-1] + v2[i])

leader = 0
cnt = 0
for i in range(1, len(pos_a)):
    if pos_a[i] > pos_b[i]:
        now = 1
    elif pos_a[i] < pos_b[i]:
        now = 2
    else:
        now = 0

    if now == 0:
        continue
    
    if leader == 0:
        leader = now
    elif leader != now:
        cnt += 1
        leader = now

print(cnt)
