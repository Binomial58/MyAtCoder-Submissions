s = list(map(str, input().split()))
R = set()
for t in s:
    if "@" not in t:
        continue
    now = []
    for j in range(len(t)):
        if t[j] == "@":
            now.append([])
        elif len(now) != 0:
            now[-1].append(t[j])
    for n in now:
        if len(n) != 0:
            R.add("".join(n))
    # print(now)
R = list(R)
R.sort()
for r in R:
    print(r)
