from collections import deque

q = int(input())
Q = deque()
R = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        Q.append(query[1])
    else:
        R.append(Q.popleft())
for r in R:
    print(r)
