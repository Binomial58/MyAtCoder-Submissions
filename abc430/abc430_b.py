n, m = map(int, input().split())
S = [list(input()) for _ in range(n)]
D = set()
for i in range(n - m + 1):
    for j in range(n - m + 1):
        T = []
        for a in range(i, i + m):
            for b in range(j, j + m):
                T.append(S[a][b])
        D.add("".join(T))
print(len(D))
