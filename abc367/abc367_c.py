from itertools import product
N,K=map(int, input().split())
R=list(map(int, input().split()))
W=[]
for p in product(range(1,max(R)+1), repeat=N):
    c=0
    if sum(p)%K==0:
        for i in range(N):
            if p[i]>R[i]:
                c=1
        if c==0:
            W.append(p)
W.sort()
for w in W:
    print(*w)