n = int(input())
A = []
C = []
D = dict()
for i in range(n):
    a, c = map(int, input().split())
    A.append(a)
    C.append(c)
    D[a] = i + 1
A, C = zip(*sorted(zip(A, C), reverse=True))
a = A[0]
c = C[0]
R = []
R.append(D[a])
A = [A[i] for i in range(1, n)]
C = [C[i] for i in range(1, n)]
Cm = [C[i] for i in range(len(C))]
Cm[0] = min(c, C[0])
for i in range(1, len(C)):
    Cm[i] = min(Cm[i], Cm[i - 1])
# print(C)
# print(Cm)
for k in range(len(C)):
    if Cm[k] >= C[k]:
        R.append(D[A[k]])
R.sort()
print(len(R))
print(*R)
