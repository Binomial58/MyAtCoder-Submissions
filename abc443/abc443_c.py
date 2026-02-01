n, t = map(int, input().split())
A = list(map(int, input().split()))
now = 0
time = 0
for i in range(n):
    if time < A[i]:
        now += A[i] - time
        time = A[i] + 100
    # print(A[i], now, time)
now += max(t - time, 0)
print(now)
