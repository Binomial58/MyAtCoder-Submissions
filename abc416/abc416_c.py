import itertools
n,k,x=map(int, input().split())
S=[]
T=[]
for i in range(n):
    s=input()
    S.append(s)
P= list(itertools.product(S, repeat=k))
P.sort()
for p in P:
    T.append("".join(p))
T.sort()
print(T[x-1])