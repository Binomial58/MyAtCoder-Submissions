h, w, n = map(int, input().split())
A = []
B = []
C = [i for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
Sa = list(set(A))
Sb = list(set(B))
Sa.sort()
Sb.sort()
Da = dict()
Db = dict()
i = 1
for a in Sa:
    Da[a] = i
    i += 1
i = 1
for b in Sb:
    Db[b] = i
    i += 1
Z = zip(A, B, C)
Zs = sorted(Z, key=lambda x: x[0])
As = [Da[Zs[i][0]] for i in range(n)]
Bs = [Zs[i][1] for i in range(n)]
Cs = [Zs[i][2] for i in range(n)]
Z = zip(As, Bs, Cs)
Zs = sorted(Z, key=lambda x: x[1])
As = [Zs[i][0] for i in range(n)]
Bs = [Db[Zs[i][1]] for i in range(n)]
Cs = [Zs[i][2] for i in range(n)]
Z = zip(As, Bs, Cs)
# print(Zs)
Zs = sorted(Z, key=lambda x: x[2])
# print(Zs)
for i in range(n):
    print(Zs[i][0], Zs[i][1])
