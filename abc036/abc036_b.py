n = int(input())
S = []
T = [[] for i in range(n)]
for i in range(n):
    S.append(input())
for i in range(n):
    for j in range(n - 1, -1, -1):
        T[i].append(S[j][i])
for t in T:
    print("".join(t))
