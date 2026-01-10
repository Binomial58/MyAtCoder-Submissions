from collections import deque

n = int(input())
V = [[] for i in range(n)]
Done = [False for i in range(n)]
Q = deque()
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        Done[i] = True
        Q.append(i)
    else:
        V[a - 1].append(i)
        V[b - 1].append(i)
while Q:
    q = Q.pop()
    for v in V[q]:
        if not Done[v]:
            Q.append(v)
            Done[v] = True
count = 0
for d in Done:
    if d:
        count += 1
print(count)
