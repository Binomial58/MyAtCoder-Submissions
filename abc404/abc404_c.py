from collections import deque

n, m = map(int, input().split())
E = [[] for i in range(n)]
# 次数を管理するもの
D = [0 for i in range(n)]
Done = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)
    D[a - 1] += 1
    D[b - 1] += 1
if D.count(2) != n:
    print("No")
    exit()
Q = deque()
Q.append(0)
while len(Q) != 0:
    q = Q.popleft()
    Done[q] += 1
    for i in E[q]:
        if Done[i] == 0:
            Q.append(i)
if 0 in Done:
    print("No")
else:
    print("Yes")
