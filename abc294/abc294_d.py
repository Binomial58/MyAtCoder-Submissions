import heapq

n, q = map(int, input().split())
P = []
heapq.heapify(P)
# まだ受付に呼ばれていない最も小さい番号
j = 1
D = set()
R = []
for i in range(q):
    E = list(map(int, input().split()))
    if E[0] == 1:
        heapq.heappush(P, j)
        j += 1
    elif E[0] == 2:
        x = E[1]
        D.add(x)
    else:
        while len(P) != 0:
            y = heapq.heappop(P)
            if y not in D:
                R.append(y)
                break
        heapq.heappush(P, y)
    # print("------")
    # print(R)
    # print(D)
    # print(P)
    # print("------")
for r in R:
    print(r)
