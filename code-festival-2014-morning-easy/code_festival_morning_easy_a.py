n = int(input())
A = list(map(int, input().split()))
s = 0
for i in range(1, n):
    s += A[i] - A[i - 1]
print(s / (n - 1))
