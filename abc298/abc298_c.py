import heapq

n = int(input())
q = int(input())
Q = [[] for i in range(n)]
for i in range(n):
    heapq.heapify(Q[i])
B = dict()
Bs = dict()
que = []
for k in range(q):
    que.append(list(map(int, input().split())))

for query in que:
    if query[0] == 1:
        i, j = query[1], query[2]
        if i not in B:
            B[i] = [j]
            Bs[i] = {j}
            heapq.heapify(B[i])
        else:
            if j not in Bs[i]:
                heapq.heappush(B[i], j)
            Bs[i].add(j)
        heapq.heappush(Q[j - 1], i)
    elif query[0] == 2:
        i = query[1]
        # print(B)
        # print(Q)
        T = Q[i - 1]
        T.sort()
        print(*T)
    else:
        i = query[1]
        # print(B)
        # print(Q)
        T = list(B[i])
        T.sort()
        print(*T)
