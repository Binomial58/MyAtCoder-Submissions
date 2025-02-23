import collections
N=int(input())
K=[]
A=[]
for _ in range(N):
    T=list(map(int, input().split()))
    K.append(T[0])
    A.append(T[1:])
maxc=0
for a in range(N):
    for b in range(a+1,N):
        C=0
        if a!=b:
           X=collections.Counter(A[a])
           Y=collections.Counter(A[b])
           Z=set(A[a])&set(A[b])
           for z in Z:
               C+=X[z]*Y[z]
        maxc=max(C/(len(A[a])*len(A[b])),maxc)
print(maxc)