n = int(input())
A = list(map(int, input().split()))
A.sort()
now = A[0] + 1
for i in range(1, n):
    now *= A[i] - A[i - 1] + 1
    now %= 10**9 + 7
print(now)
