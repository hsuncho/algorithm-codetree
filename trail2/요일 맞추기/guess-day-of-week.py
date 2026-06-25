m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def get_total_days(m, d):
    total = 0
    
    for i in range(1, m):
        total += num_of_days[i]
    
    total += d
    return total

start = get_total_days(m1, d1)
end = get_total_days(m2, d2)
diff = end - start

print(days[diff % 7])