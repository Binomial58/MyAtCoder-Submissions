import heapq

n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
count = 0
time = [-1 for i in range(n)]
Q = []
for i in range(n):
    heapq.heappush(Q, [T[i], i])
while count != n:
    q = heapq.heappop(Q)
    if time[q[1]] == -1:
        time[q[1]] = q[0]
        j = q[1] + 1
        if j == n:
            j = 0
        heapq.heappush(Q, [time[q[1]] + S[q[1]], j])
        count += 1
for t in time:
    print(t)
