n, k = map(int, input().split())
C = list(map(int, input().split()))
D = dict()
for i in range(k):
    if C[i] in D:
        D[C[i]] += 1
    else:
        D[C[i]] = 1
m = len(D)
for i in range(n - k):
    D[C[i]] -= 1
    if D[C[i]] == 0:
        del D[C[i]]
    if C[i + k] in D:
        D[C[i + k]] += 1
    else:
        D[C[i + k]] = 1
    # print(D)
    m = max(m, len(D))
print(m)
