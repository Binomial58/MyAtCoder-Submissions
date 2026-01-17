import math

n = int(input())
A = list(map(int, input().split()))
B = []
for i in range(1, n):
    B.append(abs(A[i] - A[i - 1]))
if len(B) == 1:
    g = B[0]
else:
    g = math.gcd(B[0], B[1])
for i in range(2, n - 1):
    g = math.gcd(g, B[i])
if g == 1:
    print(2)
else:
    print(1)
# print(g)
