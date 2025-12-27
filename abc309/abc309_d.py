from collections import deque

n1, n2, m = map(int, input().split())
V1 = [set() for i in range(n1)]
V2 = [set() for j in range(n2)]
Vd1 = [10**10 for i in range(n1)]
Vd2 = [10**10 for i in range(n2)]
for i in range(m):
    a, b = map(int, input().split())
    if a > n1:
        V2[a - n1 - 1].add(b - n1 - 1)
        V2[b - n1 - 1].add(a - n1 - 1)
    else:
        V1[a - 1].add(b - 1)
        V1[b - 1].add(a - 1)
Q = deque()
Vd1[0] = 0
Q.append(0)
while len(Q) != 0:
    q = Q.popleft()
    for v in V1[q]:
        if Vd1[q] + 1 < Vd1[v]:
            Vd1[v] = Vd1[q] + 1
            Q.append(v)
Q = deque()
Vd2[n2 - 1] = 0
Q.append(n2 - 1)
while len(Q) != 0:
    q = Q.popleft()
    for v in V2[q]:
        if Vd2[q] + 1 < Vd2[v]:
            Vd2[v] = Vd2[q] + 1
            Q.append(v)
# print(V1)
# print(V2)
# print(Vd1)
# print(Vd2)
print(max(Vd1) + max(Vd2) + 1)
