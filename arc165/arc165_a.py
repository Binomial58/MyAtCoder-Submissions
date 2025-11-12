from collections import defaultdict


def prime_factorize(N):
    p = defaultdict(int)
    while N % 2 == 0:
        p[2] += 1
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            p[f] += 1
            N //= f
        else:
            f += 2
    if N != 1:
        p[N] += 1
    return p


t = int(input())
R = []
for i in range(t):
    n = int(input())
    S = set(prime_factorize(n))
    p = 1
    if len(S) == 1:
        R.append("No")
    else:
        R.append("Yes")
for r in R:
    print(r)
