N=int(input())
S=[]
L=[]
T=""
for _ in range(N):
    s=input()
    S.append(s)
    L.append(len(s))
L,S=zip(*sorted(zip(L,S)))
for _ in range(N):
    T+=S[_]
print(T)