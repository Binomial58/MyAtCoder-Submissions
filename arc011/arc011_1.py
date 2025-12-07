m, n, N = map(int, input().split())
now = N
N = 0
count = now
while now >= m:
    d = now
    now = (d // m) * n
    N = d % m
    count += now
    # print(now, N)
    now += N
print(count)
