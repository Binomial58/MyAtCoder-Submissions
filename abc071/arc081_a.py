from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
# print(C)
B = list(set(A))
B.sort(reverse=True)
now = 0
L = [0, 0, 0]
for b in B:
    if C[b] >= 4:
        L[now] = b
        L[now + 1] = b
        break
    elif C[b] >= 2:
        L[now] = b
        now += 1
    if now == 2:
        break
print(L[0] * L[1])
