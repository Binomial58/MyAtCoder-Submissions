n, m = map(int, input().split())
D = [i + 1 for i in range(n)]
now = 0
for i in range(m):
    d = int(input())
    if d != now:
        di = D.index(d)
        D[di] = now
        now = d
    # print(D)
for d in D:
    print(d)
