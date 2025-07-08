N,M=map(int, input().split())
V=[]
W=[]
for i in range(N):
    A=list(map(int, input().split()))
    V.append(A[0])
    W.append(A[2:])
for a in range(N):
    for b in range(N):
        if a!=b:
            x=set(W[a])
            y=set(W[b])
            if V[a]>=V[b]:
                if x<=y:
                    if V[a]>V[b] or y>x:
                        print("Yes")
                        exit()
print("No") 