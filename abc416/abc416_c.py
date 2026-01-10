from more_itertools import distinct_permutations

n, k, x = map(int, input().split())
S = [input() for i in range(n)]
A = []
for i in range(n):
    for j in range(k):
        A.append(i)
R = []
# print(A)
for v in distinct_permutations(A, k):
    N = []
    for i in v:
        N.append(S[i])
    R.append("".join(N))
    # print(v)
R.sort()
print(R[x - 1])
