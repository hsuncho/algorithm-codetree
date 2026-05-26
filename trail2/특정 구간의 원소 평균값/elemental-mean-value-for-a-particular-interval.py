n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    total = 0  # 여기서 초기화

    for j in range(i, n):
        total += arr[j]
        length = j - i + 1

        if total % length == 0:
            avg = total // length

            for k in range(i, j + 1):
                if arr[k] == avg:
                    cnt += 1
                    break

print(cnt)