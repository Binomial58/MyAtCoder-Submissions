import itertools

n = int(input())
A = ["a", "b", "c"] * n
R = set()
for v in itertools.combinations(A, n):
    R.add("".join(v))
R = list(R)
R.sort()
for r in R:
    print(r)
