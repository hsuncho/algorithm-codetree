n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

people = []
for i in range(n):
    score = 1 if c[i] == 'G' else 2
    people.append((x[i], score))

people.sort()

i = 0
current = 0
result = 0
for j in range(n):
    current += people[j][1]

    while people[j][0] - people[i][0] > k:
        current -= people[i][1]
        i += 1

    result = max(result, current)
print(result)


