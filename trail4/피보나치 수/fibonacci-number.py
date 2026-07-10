N = int(input())

# Please write your code here.
def fibbo(N):
    if N <= 1:
        return N
    prev, cur = 0, 1
    for _ in range(2, N+1):
        prev, cur = cur, prev + cur
    return cur
print(fibbo(N))