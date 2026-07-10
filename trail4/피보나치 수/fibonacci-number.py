N = int(input())

# Please write your code here.
def fibbo(N):
    if N <= 1:
        return N
    else:
        return fibbo(N-1) + fibbo(N-2)
print(fibbo(N))