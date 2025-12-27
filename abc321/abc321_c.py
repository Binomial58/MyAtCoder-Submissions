k = int(input())
N = []
for i in range(1 << 10):
    now = []
    for j in range(10):
        if (i >> j) & 1:
            now.append(str(j))
    now.sort(reverse=True)
    if len(now) != 0:
        N.append(int("".join(now)))
    # print(i)
N.sort()
print(N[k])
