n = int(input())

# Please write your code here.
def stairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    return stairs(n-2) + stairs(n-3)
print(stairs(n))
