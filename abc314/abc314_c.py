n, m = map(int, input().split())
s = input()
C = list(map(int, input().split()))
D = [-1 for i in range(m)]
T = []
S = [[] for i in range(m)]
for i in range(n):
    S[C[i] - 1].append(s[i])
    D[C[i] - 1] += 1
for i in range(n):
    S[C[i] - 1].append(s[i])
for i in range(n):
    T.append(S[C[i] - 1][D[C[i] - 1]])
    D[C[i] - 1] += 1
print("".join(T))
