n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

ans = 0
for i in range(n):
    running_time = [0] * 1001

    for j in range(n):
        if i == j:
            continue
        
        for t in range(a[j], b[j]):
            running_time[t] = 1
    ans = max(sum(running_time), ans)
print(ans)