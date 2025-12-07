import math

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
Pi = [i for i in range(1, n + 1)]
Qi = [i for i in range(1, n + 1)]
p = 1
q = 1
for i in range(n):
    p += Pi.index(P[i]) * math.factorial(n - i - 1)
    Pi.remove(P[i])
    q += Qi.index(Q[i]) * math.factorial(n - i - 1)
    Qi.remove(Q[i])
print(abs(p - q))
