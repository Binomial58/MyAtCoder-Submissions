from collections import deque

q = int(input())
Q = deque()
R = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        c = query[2]
        # Qに対して(数の種類,個数)を右から追加する
        Q.append([x, c])
    else:
        c = query[1]
        now = 0
        nows = 0
        while now != c:
            pq = Q.popleft()
            if now + pq[1] <= c:
                now += pq[1]
                nows += pq[0] * pq[1]
            else:
                pq[1] -= c - now
                nows += pq[0] * (c - now)
                now = c
                Q.appendleft([pq[0], pq[1]])
        R.append(nows)
    # print(Q)
for r in R:
    print(r)
