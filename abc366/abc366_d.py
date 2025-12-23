# 3次元累積和
n = int(input())
A = [[[0 for i in range(n + 1)] for i in range(n + 1)]]
Ans = []
for i in range(n):
    B = [[0 for i in range(n + 1)]]
    for j in range(n):
        C = list(map(int, input().split()))
        B.append([0] + C)
    A.append(B)
# print(A)
# Aの累積和を計算するパート
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(1, n + 1):
            A[x][y][z] += A[x][y][z - 1]
for x in range(n + 1):
    for z in range(n + 1):
        for y in range(1, n + 1):
            A[x][y][z] += A[x][y - 1][z]
for z in range(n + 1):
    for y in range(n + 1):
        for x in range(1, n + 1):
            A[x][y][z] += A[x - 1][y][z]
q = int(input())
for i in range(q):
    now = 0
    query = list(map(int, input().split()))
    L = [query[0], query[2], query[4]]
    R = [query[1], query[3], query[5]]
    now += A[R[0]][R[1]][R[2]]
    now -= A[R[0]][R[1]][L[2] - 1]
    now -= A[R[0]][L[1] - 1][R[2]]
    now -= A[L[0] - 1][R[1]][R[2]]
    now += A[L[0] - 1][L[1] - 1][R[2]]
    now += A[L[0] - 1][R[1]][L[2] - 1]
    now += A[R[0]][L[1] - 1][L[2] - 1]
    now -= A[L[0] - 1][L[1] - 1][L[2] - 1]
    Ans.append(now)
for a in Ans:
    print(a)
# print(A)
