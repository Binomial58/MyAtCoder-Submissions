n = int(input())
# N=0
A = [["#"]]
# N=1
B = [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]
# N=2
k = 3**1
C = [B[i % k] for i in range(k * 3)]
for i in range(k):
    C[i] = C[i] + C[i] + C[i]
for i in range(k):
    C[i + k] = C[i + k] + ["." for i in range(k)] + C[i + k]
for i in range(k):
    C[i + k * 2] = C[i + k * 2] + C[i + k * 2] + C[i + k * 2]
# N=3
k = 3**2
D = [C[i % k] for i in range(k * 3)]
for i in range(k):
    D[i] = D[i] + D[i] + D[i]
for i in range(k):
    D[i + k] = D[i + k] + ["." for i in range(k)] + D[i + k]
for i in range(k):
    D[i + k * 2] = D[i + k * 2] + D[i + k * 2] + D[i + k * 2]
# N=4
k = 3**3
E = [D[i % k] for i in range(k * 3)]
for i in range(k):
    E[i] = E[i] + E[i] + E[i]
for i in range(k):
    E[i + k] = E[i + k] + ["." for i in range(k)] + E[i + k]
for i in range(k):
    E[i + k * 2] = E[i + k * 2] + E[i + k * 2] + E[i + k * 2]
# N=5
k = 3**4
F = [E[i % k] for i in range(k * 3)]
for i in range(k):
    F[i] = F[i] + F[i] + F[i]
for i in range(k):
    F[i + k] = F[i + k] + ["." for i in range(k)] + F[i + k]
for i in range(k):
    F[i + k * 2] = F[i + k * 2] + F[i + k * 2] + F[i + k * 2]
# N=6
k = 3**5
G = [F[i % k] for i in range(k * 3)]
for i in range(k):
    G[i] = G[i] + G[i] + G[i]
for i in range(k):
    G[i + k] = G[i + k] + ["." for i in range(k)] + G[i + k]
for i in range(k):
    G[i + k * 2] = G[i + k * 2] + G[i + k * 2] + G[i + k * 2]
P = [A, B, C, D, E, F, G]
for p in P[n]:
    print("".join(p))
