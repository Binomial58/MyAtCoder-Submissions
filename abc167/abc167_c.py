n, m, x = map(int, input().split())
A = []
C = []
for i in range(n):
    B = list(map(int, input().split()))
    A.append(B[1:])
    C.append(B[0])
# print(A)
M = 10**10
for i in range(1 << n):
    now = 0
    X = [0 for k in range(m)]
    for j in range(n):
        if (i >> j) & 1:
            for k in range(m):
                X[k] += A[j][k]
            now += C[j]
    flag = True
    for t in X:
        if t < x:
            flag = False
    if flag:
        M = min(M, now)
    # print(X)
if M == 10**10:
    print(-1)
else:
    print(M)
