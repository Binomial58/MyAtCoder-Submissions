n = int(input())
A, B = [], []
S = []
C = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for i in range(n):
    S.append([(A[i] * 10**100 // (A[i] + B[i])), i + 1])
# print(S)
S.sort(key=lambda x: (-x[0], x[1]))
T = []
for s in S:
    T.append(s[1])
print(*T)
