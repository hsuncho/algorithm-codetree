N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

arr = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if min(abs(a1 - i), N - abs(a1 - i)) <= 2 and min(abs(b1 - j), N - abs(b1 - j)) <= 2 and min(abs(c1 - k), N - abs(c1 - k)) <= 2:
                arr.append((i, j, k))
            if min(abs(a2 - i), N - abs(a2 - i)) <= 2 and min(abs(b2 - j), N - abs(b2 - j)) <= 2 and min(abs(c2 - k), N - abs(c2 - k)) <= 2:
                arr.append((i, j, k))

s = set(arr)
print(len(s))