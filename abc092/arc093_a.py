n = int(input())
A = list(map(int, input().split()))
A = [0] + A + [0]
# print(A)
l = 0
for i in range(n + 1):
    l += abs(A[i + 1] - A[i])
for i in range(1, n + 1):
    print(l - abs(A[i] - A[i - 1]) - abs(A[i + 1] - A[i]) + abs(A[i + 1] - A[i - 1]))
# print(l)
