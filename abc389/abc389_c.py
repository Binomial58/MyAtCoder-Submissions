from collections import deque

q = int(input())
Q = deque()
R = []
now = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if len(Q) == 0:
            Q.append([0, query[1]])
        else:
            Q.append([Q[-1][1], Q[-1][1] + query[1]])
    elif query[0] == 2:
        t = Q.popleft()
        now = t[1]
    else:
        R.append(Q[query[1] - 1][0] - now)
    # print(Q, now)
for r in R:
    print(r)
