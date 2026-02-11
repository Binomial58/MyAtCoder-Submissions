h, w, n = map(int, input().split())
G = []
X = dict()
Y = dict()
for i in range(h):
    X[i + 1] = set()
for i in range(w):
    Y[i + 1] = set()
for i in range(n):
    x, y = map(int, input().split())
    G.append([x, y])
    X[x].add(i)
    Y[y].add(i)
# print(G)
# print(X)
# print(Y)
q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        print(len(X[x]))
        for xi in X[x]:
            Y[G[xi][1]].remove(xi)
        X[x] = set()
    else:
        y = query[1]
        print(len(Y[y]))
        for yi in Y[y]:
            X[G[yi][0]].remove(yi)
        Y[y] = set()
