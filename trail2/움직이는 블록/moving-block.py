n = int(input())
blocks = [int(input()) for _ in range(n)]

avg = sum(blocks) // n
cnt = 0
for b in blocks:
    if b > avg:
        cnt += b - avg

print(cnt)    