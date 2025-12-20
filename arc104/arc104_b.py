n, s = map(str, input().split())
n = int(n)
count = 0
A = [0 for i in range(n + 1)]
G = [0 for i in range(n + 1)]
C = [0 for i in range(n + 1)]
T = [0 for i in range(n + 1)]
for i in range(n):
    if s[i] == "A":
        A[i + 1] += 1
    elif s[i] == "G":
        G[i + 1] += 1
    elif s[i] == "C":
        C[i + 1] += 1
    else:
        T[i + 1] += 1
for i in range(1, n + 1):
    A[i] += A[i - 1]
    G[i] += G[i - 1]
    C[i] += C[i - 1]
    T[i] += T[i - 1]
for l in range(n):
    for r in range(n):
        if l < r:
            a = A[r + 1] - A[l]
            g = G[r + 1] - G[l]
            c = C[r + 1] - C[l]
            t = T[r + 1] - T[l]
            if a == t and g == c:
                count += 1
print(count)