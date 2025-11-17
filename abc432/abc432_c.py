n, x, y = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
maxc = y * A[0]
count = A[0]
a = 10**10

for i in range(1, n):
    t = y * A[i] - maxc
    if t // (y - x) > A[i]:
        print(-1)
        exit()
    if t % (y - x) != 0:
        print(-1)
        exit()
    count += A[i] - t // (y - x)
print(count)
