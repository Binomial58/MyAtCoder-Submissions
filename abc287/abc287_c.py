from collections import deque

n, m = map(int, input().split())
V = [set() for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    V[u - 1].add(v - 1)
    V[v - 1].add(u - 1)
if n != m + 1:
    print("No")
    exit()
# print(V)
d1 = 0
d2 = 0
for v in V:
    if len(v) == 1:
        d1 += 1
    elif len(v) == 2:
        d2 += 1
    else:
        print("No")
        exit()
if d1 != 2:
    print("No")
    exit()
isDone = [False for i in range(n)]
Q = deque()
Q.append(0)
isDone[0] = True
while len(Q) != 0:
    q = Q.pop()
    for v in V[q]:
        if not isDone[v]:
            Q.append(v)
            isDone[v] = True
for i in isDone:
    if not i:
        print("No")
        exit()
print("Yes")
