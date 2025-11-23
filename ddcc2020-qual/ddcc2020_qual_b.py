import bisect

n = int(input())
A = list(map(int, input().split()))
sumA = [0 for i in range(n)]
sumA[0] = A[0]
a = sum(A) // 2
for i in range(1, n):
    sumA[i] = sumA[i - 1] + A[i]
li = bisect.bisect_left(sumA, a)
# print(li, ri)
# print(A[:li], A[li:])
# print(A[: li + 1], A[li + 1 :])
# print(abs(sum(A[li:]) - sum(A[:li])))
# print(abs(sum(A[li + 1 :]) - sum(A[: li + 1])))
print(min(abs(sum(A[li:]) - sum(A[:li])), abs(sum(A[li + 1 :]) - sum(A[: li + 1]))))
