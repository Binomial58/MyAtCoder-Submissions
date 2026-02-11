from collections import deque

n, k = map(int, input().split())
A = []
V = [set() for i in range(n)]
for i in range(n):
    A.append(list(map(int, input().split())))
D = [[10**9 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            V[i].add(j)
            D[i][j] = 1
for i in range(n):
    for j in range(n):
        if D[i][j] == 10**9:
            # Visited = [False for i in range(n)]
            # Visited[i] = True
            Q = deque()
            Turn = [10**9 for i in range(n)]
            Q.append((i, 0))
            while len(Q) != 0:
                # print(Q)
                q, c = Q.pop()
                c += 1
                for v in V[q]:
                    if c < Turn[v]:
                        Turn[v] = c
                        Q.append((v, c))
            D[i][j] = Turn[j]
            # print(Turn)

# print(V)
# print(D)
q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    s %= n
    t %= n
    if D[s][t] == 10**9:
        print(-1)
    else:
        print(D[s][t])
    # print(s, t)
