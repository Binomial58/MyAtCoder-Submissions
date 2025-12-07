from collections import deque

n, m = map(int, input().split())
V = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    V[a - 1].add(b - 1)
    V[b - 1].add(a - 1)
Done = [0 for i in range(n)]
for i in range(n):
    if Done[i] == 0:
        Q = deque()
        Q.append(i)
        Done[i] += 1
        while len(Q) != 0:
            # print(Q)
            # print(Done)
            q = Q.popleft()
            for v in V[q]:
                if Done[v] == 0:
                    Q.append(v)
                Done[v] += 1
                V[v].remove(q)
print(sum(Done) - n)
