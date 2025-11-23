n = int(input())
A = list(map(int, input().split()))
sumA = [0 for i in range(n)]
sumA[0] = A[0]
for i in range(1, n):
    sumA[i] = sumA[i - 1] + A[i]
count = 0
for i in range(n):
    count += A[i] * (sumA[-1] - sumA[i])
    count %= 10**9 + 7
print(count)
