n = int(input())
A = list(map(int, input().split()))
As = [A[0]]
for i in range(1, n):
    As.append(As[-1] + A[i])
now = 0
for i in range(n):
    now += A[i] * (As[-1] - As[i])
print(now)
