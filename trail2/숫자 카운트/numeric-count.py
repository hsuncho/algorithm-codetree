n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
answer = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            
            candidate = str(i) + str(j) + str(k)
            possible = True

            for arr_idx in range(n):
                question = str(a[arr_idx])

                chk_cnt1 = 0
                chk_cnt2 = 0

                for str_idx in range(3):
                    if candidate[str_idx] == question[str_idx]:
                        chk_cnt1 += 1
                    elif candidate[str_idx] in question:
                        chk_cnt2 += 1

                if chk_cnt1 != b[arr_idx] or chk_cnt2 != c[arr_idx]:
                    possible = False
                    break
                
            if possible:
                answer += 1

print(answer)