N,D=map(int, input().split())
T=[]
L=[]
for _ in range(N):
    t,l=map(int, input().split())
    T.append(t)
    L.append(l)
for i in range(1,D+1):
    maxL=0
    for k in range(N):
        L[k]+=1
        maxL=max(maxL,T[k]*L[k])
    print(maxL)