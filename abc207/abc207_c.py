n = int(input())
T = []
L = []
R = []
count = 0
for i in range(n):
    t, l, r = map(int, input().split())
    if t == 2 or t == 4:
        R.append(r - 0.25)
    else:
        R.append(r)
    if t == 3 or t == 4:
        L.append(l + 0.25)
    else:
        L.append(l)
for a in range(n):
    for b in range(n):
        if a > b:
            if (R[a] - L[b]) * (R[b] - L[a]) >= 0:
                count += 1
print(count)
