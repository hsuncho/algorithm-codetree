ability = list(map(int, input().split()))
# Please write your code here.
answer = 1000000
total = sum(ability)
n = len(ability)
for i in range(n):
    for j in range(i + 1, n):
        team1 = [ability[i], ability[j]]

        for k in range(n):
            for r in range(k + 1, n):
                if ability[k] in team1 or ability[r] in team1:
                    continue
                sum1 = ability[i] + ability[j]
                sum2 = ability[k] + ability[r]
                sum3 = total - sum1 - sum2
                answer = min(max(sum1, sum2, sum3)-min(sum1, sum2, sum3), answer)
print(answer)