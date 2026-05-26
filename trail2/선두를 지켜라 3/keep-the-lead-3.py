N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

pos_a = [0]
pos_b = [0]

for i in range(N):
    for _ in range(t[i]):
        pos_a.append(pos_a[-1] + v[i])

for i in range(M):
    for _ in range(t2[i]):
        pos_b.append(pos_b[-1] + v2[i])

leader = 0 # 0 = 공동. 1 = A. 2 = B
cnt = 0
for i in range(len(pos_a)):
    if pos_a[i] > pos_b[i]:
        now = 1
    elif pos_a[i] < pos_b[i]:
        now = 2
    else:
        now = 0

    if leader != now:
        cnt += 1
        leader = now

print(cnt)