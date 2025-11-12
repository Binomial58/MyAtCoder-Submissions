n, m = map(int, input().split())
account = 0
pcount = 0
WA = [0 for i in range(n)]
AC = [True for i in range(n)]
for i in range(m):
    p, s = map(str, input().split())
    if s == "WA":
        WA[int(p) - 1] += 1
    else:
        if AC[int(p) - 1]:
            AC[int(p) - 1] = not AC[int(p) - 1]
            account += 1
            pcount += WA[int(p) - 1]
print(account, pcount)
