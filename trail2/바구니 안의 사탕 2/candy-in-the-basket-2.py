N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)


paired = sorted(zip(pos, candy))
sorted_pos = [x[0] for x in paired]
sorted_candy = [x[1] for x in paired]

window_sum = 0
max_val=0
left = 0

for right in range(N):
    window_sum += sorted_candy[right]

    while sorted_pos[right] - sorted_pos[left] > 2*K:
        window_sum -= sorted_candy[left]
        left += 1

    max_val = max(max_val, window_sum)

print(max_val)