n = int(input())
A = list(map(int, input().split()))
now = 0
for i in range(n):
    if i % 2 == 0:
        now += A[i]
print(now)
