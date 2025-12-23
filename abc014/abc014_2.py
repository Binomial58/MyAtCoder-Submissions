n, x = map(int, input().split())
A = list(map(int, input().split()))
B = []
while x >= 2:
    B.append(x % 2)
    x //= 2
B.append(x)
B = B + [0 for i in range(n - len(B))]
now = 0
for i in range(n):
    now += B[i] * A[i]
print(now)
# print(B)
