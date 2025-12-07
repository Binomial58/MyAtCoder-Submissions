n = int(input())
A = list(map(int, input().split()))
A.sort()
As = [A[i] for i in range(n)]
for i in range(1, n):
    As[i] += As[i - 1]
count = 0

for i in range(n - 1):
    s = As[-1] - As[i]
    count += s - A[i] * (n - i - 1)
# print(A)
# print(As)
print(count)
