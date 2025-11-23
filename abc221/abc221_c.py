import itertools

n = input()
N = [n[i] for i in range(len(n))]
I = [i for i in range(len(n))]
Is = set(I)
l = len(n) // 2
if len(n) % 2 != 0:
    l += 1
now = 0
for v in itertools.combinations(I, l):
    u = Is - set(v)
    A = [int(N[a]) for a in v]
    B = [int(N[b]) for b in u]
    A.sort()
    B.sort()
    x = 0
    y = 0
    for i in range(len(A)):
        x += A[i] * 10**i
    for i in range(len(B)):
        y += B[i] * 10**i
    # print(x * y)
    now = max(now, x * y)
print(now)
