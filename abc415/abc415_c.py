t = int(input())
R = []
for _ in range(t):
    n = int(input())
    s = "0" + input()
    ok = [False] * (1 << n)
    ok[0] = True
    for i in range(1 << n):
        if not ok[i]:
            continue
        else:
            for j in range(n):
                k = i | (1 << j)
                if s[k] == "0":
                    ok[k] = True
    if ok[-1]:
        R.append("Yes")
    else:
        R.append("No")
for r in R:
    print(r)
