import bisect

n = int(input())
A = []
B = []
T = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(a / b)
for i in range(1, n):
    T[i] += T[i - 1]
d = bisect.bisect(T, T[-1] / 2)
dt = T[-1] / 2 - T[d - 1]
# print(d, dt)
# print(T)
if n == 1:
    print(a / 2)
else:
    print(sum(A[:d]) + dt * B[d])
