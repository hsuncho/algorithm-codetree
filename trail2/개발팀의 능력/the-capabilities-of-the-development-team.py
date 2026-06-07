arr = list(map(int, input().split()))

# Please write your code here.
import sys
answer = sys.maxsize
n = len(arr)
total = sum(arr)
for i in range(n):
    for j in range(i + 1, n):
        team1 = [i, j]

        for k in range(n):
            if k in team1:
                continue
            
            sum1 = arr[i] + arr[j]
            sum3 = arr[k]
            sum2 = total - sum1 - sum3

            if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
                continue
            answer = min(answer, max(sum1, sum2, sum3) - min(sum1, sum2, sum3))

if answer == sys.maxsize:
    answer = -1
print(answer)