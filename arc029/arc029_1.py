n = int(input())
T = [int(input()) for i in range(n)]
s = sum(T)
m = 10**10
for i in range(1 << n):
    now = 0
    for j in range(n):
        if (i >> j) & 1:
            now += T[j]
    d = s - now
    # print(d, now)
    m = min(m, max(d, now))
print(m)
