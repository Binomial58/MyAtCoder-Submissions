import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Am = [A[i] for i in range(n)]
for i in range(1, n):
    Am[i] = min(A[i], Am[i - 1])
# print(Am)
Am = Am[::-1]
# print(Am)
for i in range(m):
    # print(Am, B[i])
    d = n - bisect.bisect_right(Am, B[i])
    # print(bisect.bisect_right(Am, B[i]))
    if d == n:
        print(-1)
    else:
        print(d + 1)
