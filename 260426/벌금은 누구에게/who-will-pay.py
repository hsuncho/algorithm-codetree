N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
cnt = [0] * N

answer = -1

for s in student:
    cnt[s-1] += 1
    if cnt[s-1] == 3:
        answer = s

print(answer)

    

