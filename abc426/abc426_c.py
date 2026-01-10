n, q = map(int, input().split())
m = 0
Now = [1 for i in range(n)]
R = []
for i in range(q):
    x, y = map(int, input().split())
    if m >= x:
        R.append(0)
    else:
        # print(Now[m:x])
        R.append(sum(Now[m:x]))
        Now[y - 1] += sum(Now[m:x])
        m = max(x, m)
    # print(Now)
for r in R:
    print(r)
