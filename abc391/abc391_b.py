N,M=map(int, input().split())
S=[]
T=[]
for _ in range(N):
    s=input()
    S.append(s)
for _ in range(M):
    t=input()
    T.append(t)
for a in range(N-M+1):
    for b in range(N-M+1):
        C=True
        for i in range(M):
            for k in range(M):
                if T[i][k]!=S[i+a][k+b]:
                    C=False
        if C:
            print(a+1,b+1)