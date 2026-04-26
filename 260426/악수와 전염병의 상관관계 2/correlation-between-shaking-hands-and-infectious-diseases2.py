N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

handshakes.sort(key=lambda x:x[0])
infected = [0] * N
cnt = [0] * N
infected[P-1] = 1
for t, x, y in handshakes:
    infected_x = infected[x-1]
    infected_y = infected[y-1]

    if infected_x:
        cnt[x-1] += 1
    
    if infected_y:
        cnt[y-1] += 1

    if infected_x and cnt[x-1] <= K:
        infected[y-1] = 1
    
    if infected_y and cnt[y-1] <= K:
        infected[x-1] = 1

for i in infected:
    print(i, end="")



