n, q = map(int, input().split())
s = input()
now = 0
R = []
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        now += x
        now %= n
    else:
        # print(now)
        R.append(s[(x - 1 - now) % n])
for r in R:
    print(r)
