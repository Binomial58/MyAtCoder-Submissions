n = int(input())
A = list(map(int, input().split()))
num = [0 for i in range(2 * n + 1)]
for i in range(1, n + 1):
    b = 2 * i
    num[b - 1] = num[A[i - 1] - 1] + 1
    num[b] = num[A[i - 1] - 1] + 1
for i in num:
    print(i)
