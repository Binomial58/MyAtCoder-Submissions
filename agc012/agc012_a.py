n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
A = A[: 2 * n]
c = 0
for i in range(n):
    c += A[2 * i + 1]
print(c)
