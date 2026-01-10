import heapq

n = int(input())
A = list(map(int, input().split()))
heapq.heapify(A)
while len(A) != 1:
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    b %= a
    if b != 0:
        heapq.heappush(A, b)

    heapq.heappush(A, a)
print(*A)
