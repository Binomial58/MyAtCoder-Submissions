N=int(input())
S=[input() for _ in range(N)]
M=0
E=[]
for i in range(N):
    M=max(M,len(S[i]))
for k in range(N):
    L=M-len(S[k])
    S[k]+="*"*L
for a in range(M):
    A=""
    for b in range(N-1,-1,-1):
       A+=S[b][a]
    E.append(A)
for c in range(M):
    while E[c][-1]=="*":
        E[c]=E[c].rstrip("*")
    print(E[c])