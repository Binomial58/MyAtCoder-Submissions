n, m, k = map(int, input().split())
R = []
C = [0 for i in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    C[a - 1] += 1
    if C[a - 1] == m:
        R.append(a)
print(*R)
