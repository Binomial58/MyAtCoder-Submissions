import math

n, k = map(int, input().split())
A = list(map(int, input().split()))
R = []
noR = []
for i in range(n):
    if i + 1 in A:
        R.append(list(map(int, input().split())))
    else:
        noR.append(list(map(int, input().split())))
D = [10**9 for i in range(len(noR))]
for r in R:
    for i in range(len(noR)):
        nor = noR[i]
        d = math.sqrt((r[0] - nor[0]) ** 2 + (r[1] - nor[1]) ** 2)
        D[i] = min(D[i], d)
print(max(D))
