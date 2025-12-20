from collections import deque

n = int(input())
T = []
A = []
for i in range(n):
    Q = list(map(int, input().split()))
    T.append(Q[0])
    A.append(Q[2:])
Done = [False for i in range(n)]
Q = deque()
Q.append(n - 1)
Done[n - 1] = True
time = T[n - 1]
while len(Q) != 0:
    q = Q.pop()
    for a in A[q]:
        if not Done[a - 1]:
            time += T[a - 1]
            Done[a - 1] = True
            Q.append(a - 1)
# print(T)
# print(A)
print(time)
