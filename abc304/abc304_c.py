from collections import deque

n, d = map(int, input().split())
X = []
Y = []
V = [[] for i in range(n)]
Q = deque()
Done = [False for i in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for a in range(n):
    for b in range(n):
        if a > b:
            if (X[a] - X[b]) ** 2 + (Y[a] - Y[b]) ** 2 <= d**2:
                V[a].append(b)
                V[b].append(a)
Q.append(0)
Done[0] = True
# print(V)
while len(Q) != 0:
    q = Q.popleft()
    for i in V[q]:
        if not Done[i]:
            Done[i] = True
            Q.append(i)
for d in Done:
    if d:
        print("Yes")
    else:
        print("No")
# print(Done)
