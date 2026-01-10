from collections import deque

q = int(input())
Q = deque([0 for i in range(100)])
R = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        Q.append(query[1])
    else:
        R.append(Q.pop())
for r in R:
    print(r)
