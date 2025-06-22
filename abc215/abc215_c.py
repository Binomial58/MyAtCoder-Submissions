from itertools import permutations
S,K=map(str, input().split())
R=set()
for i in permutations(S):
    R.add("".join(i))
R=list(R)
R.sort()
print(R[int(K)-1])