n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

paired = sorted(zip(pos, alpha))

max_val = 0

if n == 1:
    print(0)
else:
    for left in range(n):
        g_cnt = 0
        h_cnt = 0
        
        for right in range(left, n):
            if paired[right][1] == 'G':
                g_cnt += 1
            else:
                h_cnt += 1
        
            if g_cnt * h_cnt == 0 or g_cnt == h_cnt:
                max_val = max(max_val, paired[right][0] - paired[left][0])
    print(max_val)