from collections import deque

n, x = map(int, input().split())
A = []
for i in range(n):
    L = list(map(int, input().split()))
    A.append(L[1:])
# print(A)
count = 0
for a in A[0]:
    Q = deque()
    Q.append([a, 1])
    while len(Q) != 0:
        # print(Q)
        q, j = Q.pop()
        for b in A[j]:
            if j + 1 == n:
                if q * b == x:
                    count += 1
            elif q * b <= x:
                Q.append([q * b, j + 1])
print(count)
