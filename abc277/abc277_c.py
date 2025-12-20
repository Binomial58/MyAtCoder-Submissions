from collections import deque

n = int(input())
V = dict()
for i in range(n):
    a, b = map(int, input().split())
    if a - 1 in V:
        V[a - 1].add(b - 1)
    else:
        V[a - 1] = set()
        V[a - 1].add(b - 1)
    if b - 1 in V:
        V[b - 1].add(a - 1)
    else:
        V[b - 1] = set()
        V[b - 1].add(a - 1)
# print(V)
isDone = dict()
for v in V:
    isDone[v] = False
# print(isDone)
Q = deque()
Q.append(0)
isDone[0] = True
while len(Q) != 0:
    q = Q.pop()
    if q in V:
        for v in V[q]:
            if not isDone[v]:
                Q.append(v)
                isDone[v] = True
# print(isDone)
m = 1
for v in isDone:
    if isDone[v]:
        m = max(m, v + 1)
print(m)
