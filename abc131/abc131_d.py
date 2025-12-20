from collections import deque

n = int(input())
A, B = [], []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
B, A = zip(*sorted(zip(B, A)))
Q = deque()
for i in range(n):
    Q.append([B[i], A[i]])
now = 0
for i in range(n):
    q = Q.popleft()
    if now + q[1] > q[0]:
        print("No")
        exit()
    now += q[1]
print("Yes")
