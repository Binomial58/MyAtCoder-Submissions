n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
d = 0
count = 0
for i in range(n):
    count += min(A[i], B[i])
    B[i] = max(0, B[i] - A[i])
    count += min(A[i + 1], B[i])
    A[i + 1] = max(0, A[i + 1] - B[i])
print(count)
