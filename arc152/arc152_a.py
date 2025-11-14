n, l = map(int, input().split())
A = list(map(int, input().split()))
if A.count(2) == 0:
    print("Yes")
    exit()
i = A[::-1].index(2)
i = n - i - 1
sum = 0
for j in range(i):
    sum += A[j] + 1
if l - sum >= 2:
    print("Yes")
else:
    print("No")
