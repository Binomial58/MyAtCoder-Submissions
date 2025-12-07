import itertools

X = list(map(int, input().split()))
S = []
for v in itertools.permutations(X, 3):
    S.append(sum(v))
S = list(set(S))
S.sort(reverse=True)
print(S[2])
