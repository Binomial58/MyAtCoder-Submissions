n = int(input())
A = list(map(int, input().split()))
R = []
i = 0
while i != n - 1:
    if A[i] != i + 1:
        a = A[i]
        b = A[A[i] - 1]
        P = [i + 1, A[i]]
        P.sort()
        R.append(P)
        A[i] = b
        A[a - 1] = a
    if i + 1 == A[i]:
        i += 1
print(len(R))
for r in R:
    r.sort()
    print(*r)
