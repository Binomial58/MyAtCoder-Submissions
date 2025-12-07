n, m = map(int, input().split())
K = []
# 各料理に含まれている食材の種類数
C = [0 for i in range(m)]
# 各食材が使われている料理の番号
D = [[] for i in range(n)]
for i in range(m):
    k = list(map(int, input().split()))
    k = k[1:]
    C[i] = len(k)
    K.append(k)
    for j in k:
        D[j - 1].append(i)
B = list(map(int, input().split()))
count = 0
for i in range(n):
    for d in D[B[i] - 1]:
        C[d] -= 1
        if C[d] == 0:
            count += 1
    print(count)
    # print(C)
# print(K)
# print(C)
# print(D)
