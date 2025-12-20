import heapq

n, k = map(int, input().split())
P = list(map(int, input().split()))
Q = [P[i] for i in range(k - 1)]
# print(Q)
heapq.heapify(Q)
# print(Q)
for i in range(n - k + 1):
    d = k + i - 1
    heapq.heappush(Q, P[d])
    if len(Q) > k:
        heapq.heappop(Q)
    r = heapq.heappop(Q)
    print(r)
    heapq.heappush(Q, r)
