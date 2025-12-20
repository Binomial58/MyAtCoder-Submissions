n = int(input())
X = list(map(int, input().split()))
Y = [X[i] for i in range(n)]
Y.sort()
l = Y[len(Y) // 2 - 1]
r = Y[len(Y) // 2]
# print(l, r)
D = dict()
for i in range(n):
    if i < len(Y) // 2:
        D[Y[i]] = r
    else:
        D[Y[i]] = l
# print(D)
for x in X:
    print(D[x])
