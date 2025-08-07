X=input()
n=int(input())
S=[]
T=[]
U=[i for i in range(n)]
D={}
for i in range(26):
    D[X[i]]=chr(97+i)
for i in range(n):
    s=input()
    S.append(s)
    t=""
    for a in s:
        t+=D[a]
    T.append(t)
T, U = zip(*sorted(zip(T, U)))
for u in U:
    print(S[u])