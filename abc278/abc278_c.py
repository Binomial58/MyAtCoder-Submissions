n, q = map(int, input().split())
FF = dict()
R = []
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if a not in FF:
            FF[a] = dict()
        FF[a][b] = True
    if t == 2:
        if a not in FF:
            FF[a] = dict()
        FF[a][b] = False
    if t == 3:
        if a not in FF or b not in FF:
            R.append("No")
        else:
            if b not in FF[a] or a not in FF[b]:
                R.append("No")
            else:
                if FF[a][b] and FF[b][a]:
                    R.append("Yes")
                else:
                    R.append("No")
for r in R:
    print(r)
