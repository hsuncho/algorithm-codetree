N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_B = sorted(B)
cnt = 0

for i in range(N-M+1):
    sub = A[i:i+M]
    if sorted(sub) == sorted_B:
        cnt += 1

print(cnt)

# 오류 1: in으로 부분 문자열 존재 여부만 체크 (횟수 X)
# 오류 2: 문자열 비교라 '55' in '555555'가 True여도 위치 기반 슬라이싱이 아님

# from itertools import permutations

# beautiful = set(permutations(B))
# cnt = 0

# for i in range(N-M+1):
#     sub = tuple(A[i:i+M])
#     if sub in beautiful:
#         cnt += 1
# print(cnt)