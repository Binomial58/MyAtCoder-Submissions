from collections import deque

n, m = map(int, input().split())
V = [set() for i in range(n)]
Done = [0 for i in range(n)]
count = 0
for i in range(m):
    a, b = map(int, input().split())
    V[a - 1].add(b - 1)
    V[b - 1].add(a - 1)
for i in range(n):
    if not Done[i]:
        Q = deque()
        Q.append(i)
        Done[i] = 1
        while len(Q) != 0:
            # print(Q, count)
            # print(Done)
            q = Q.popleft()
            for c in V[q]:
                if Done[c] == 0:
                    Q.append(c)
                    V[c].remove(q)
                    Done[c] = Done[q] + 1
                else:
                    V[c].remove(q)
                    count += 1
print(count)
