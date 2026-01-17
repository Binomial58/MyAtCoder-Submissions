import itertools

n, m = map(int, input().split())
T = [set() for i in range(n)]
A = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    T[a - 1].add(b - 1)
    T[b - 1].add(a - 1)
for i in range(m):
    a, b = map(int, input().split())
    A[a - 1].add(b - 1)
    A[b - 1].add(a - 1)
# print(T)
# print(A)
P = [i for i in range(n)]
for p in itertools.permutations(P):
    N = [set() for i in range(n)]
    # print(p)
    for i in range(n):
        for a in A[i]:
            N[p[i]].add(p[a])
    if N == T:
        print("Yes")
        exit()
    # print(p)
    # print(N)
print("No")
