N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

# Please write your code here.
ans = 0
for cheese in range(1, M + 1):
    possibility = True

    for i in range(S):
        person = sick_p[i]
        sick_time = sick_t[i]

        for j in range(D):
            if p[j] == person and m[j] == cheese and t[j] < sick_time:
                break
        else:
            possibility = False
            break
        
        if possibility:
            people = []
            for j in range(D):
                if m[j] == cheese:
                    people.append(p[j])
            ans = max(ans, len(people))
print(ans)