a, b, c = map(int, input().split())
minutes = 0
m, d, t = 11, 11, 11

while True:
    if m == a and d == b and t == c:
        break
    
    if a < m or (a == m and b < d) or (a == m and b == d and c < t) :
        print(-1)
        break
    
    minutes += 1
    t += 1

    if t == 60:
        d += 1
        t = 0

    if d == 24:
        m += 1
        d = 0
    
print(minutes)