n, m = map(int, input().split())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A, B = zip(*sorted(zip(A, B)))
count = 0
now = 0
# print(A)
# print(B)
while m != 0:
    j = min(m, B[now])
    m = max(0, m - B[now])
    count += A[now] * j
    # print(A[now], j)
    now += 1
print(count)
