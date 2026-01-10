n, m, q = map(int, input().split())
Auth = [set() for i in range(n)]
All = [False for i in range(n)]
R = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if not All[query[1] - 1]:
            Auth[query[1] - 1].add(query[2])
    elif query[0] == 2:
        All[query[1] - 1] = True
    else:
        if All[query[1] - 1]:
            R.append("Yes")
        else:
            if query[2] in Auth[query[1] - 1]:
                R.append("Yes")
            else:
                R.append("No")
for r in R:
    print(r)
