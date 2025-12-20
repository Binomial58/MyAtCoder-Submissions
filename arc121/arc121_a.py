n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
xmi = X.index(min(X))
ymi = Y.index(min(Y))
xMi = X.index(max(X))
yMi = Y.index(max(Y))
S = dict()
for k in range(n):
    p = k
    q = xmi
    i, a = min(p, q), max(p, q)
    if (i, a) in S:
        S[(i, a)] = max(S[(i, a)], abs(X[i] - X[a]))
    else:
        S[(i, a)] = abs(X[i] - X[a])
    q = ymi
    i, a = min(p, q), max(p, q)
    if (i, a) in S:
        S[(i, a)] = max(S[(i, a)], abs(Y[i] - Y[a]))
    else:
        S[(i, a)] = abs(Y[i] - Y[a])
    q = xMi
    i, a = min(p, q), max(p, q)
    if (i, a) in S:
        S[(i, a)] = max(S[(i, a)], abs(X[i] - X[a]))
    else:
        S[(i, a)] = abs(X[i] - X[a])
    q = yMi
    i, a = min(p, q), max(p, q)
    if (i, a) in S:
        S[(i, a)] = max(S[(i, a)], abs(Y[i] - Y[a]))
    else:
        S[(i, a)] = abs(Y[i] - Y[a])
R = []
for s in S:
    R.append(S[s])
R.sort(reverse=True)
print(R[1])
