n = int(input())
P = list(map(int, input().split()))
R = [0 for i in range(n)]
count = 0
r = 1
while count != n:
    m = max(P)
    now = 0
    for i in range(n):
        if P[i] == m:
            R[i] = r
            P[i] = 0
            count += 1
            now += 1
    r += now
for r in R:
    print(r)
