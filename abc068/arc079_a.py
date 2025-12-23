from collections import deque

n, m = map(int, input().split())
V = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    V[a - 1].append(b - 1)
    V[b - 1].append(a - 1)
Turn = [10**10 for i in range(n)]
Turn[0] = 0
Q = deque()
Q.append(0)
while len(Q) != 0:
    q = Q.pop()
    for v in V[q]:
        if Turn[q] + 1 < Turn[v] and Turn[q] != 2:
            Turn[v] = Turn[q] + 1
            Q.append(v)
            if v == n - 1:
                print("POSSIBLE")
                exit()
print("IMPOSSIBLE")
