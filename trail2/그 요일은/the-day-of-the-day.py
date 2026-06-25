m1, d1, m2, d2 = map(int, input().split())
A = input()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
num = 0

while True:
    
    if day == days.index(A):
        num += 1

    if m1 == m2 and d1 == d2:
        break
        
    day += 1
    d1 += 1

    if day >= len(days):
        day = 0

    if d1 > num_of_days[m1]:
        d1 = 1
        m1 += 1

print(num)

