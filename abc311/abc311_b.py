N,D=map(int, input().split())
S=[input() for _ in range(N)]
maxd=0
d=0
for i in range(D):
    if all(S[k][i]=="o" for k in range(N)):
        d+=1
        maxd=max(d,maxd)
    else:
        d=0
print(maxd)