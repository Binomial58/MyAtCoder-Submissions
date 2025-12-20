from collections import deque

n = int(input())
A = list(map(int, input().split()))
Q = deque()
for i in range(n):
    if i % 2 == 0:
        Q.append(A[i])
    else:
        Q.appendleft(A[i])
if n % 2 == 0:
    print(*Q)
else:
    Q = list(Q)
    print(*Q[::-1])
