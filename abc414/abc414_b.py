n = int(input())
R = []
now = 0
L = []
for i in range(n):
    c, l = map(str, input().split())
    L.append([c, int(l)])
for i in range(n):
    now += L[i][1]
    if now > 100:
        print("Too Long")
        exit()
    for j in range(L[i][1]):
        R.append(L[i][0])
print("".join(R))
