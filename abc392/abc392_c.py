N=int(input())
M=[i for i in range(1,N+1)]
P=list(map(int, input().split()))
Q=list(map(int, input().split()))
S=[]
dict1={}
for q in range(N):
    dict1[Q[q]]=M[q]
dict2={}
for p in P:
    dict2[p]=Q[p-1]
for k in range(N):
    d=dict1[k+1]
    r=P[d-1]
    s=dict2[r]
    S.append(s)
print(*S)