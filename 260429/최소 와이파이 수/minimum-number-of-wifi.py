n, m = map(int, input().split())
arr = list(map(int, input().split()))

people = [i+1 for i in range(n) if arr[i] == 1]

cnt = 0
i = 0
while i < len(people):
    wifi = people[i] + m
    cnt += 1
    while i < len(people) and people[i] <= wifi + m:
        i += 1
print(cnt)