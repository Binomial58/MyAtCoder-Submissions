N,M=map(int, input().split())
A=list(map(int, input().split()))
X=[]
S=[]
for k in range(N):
    X.append(list(map(int, input().split())))
for i in range(M):
    S.append(sum(X[j][i] for j in range(N)))
if all(S[u]>=A[u] for u in range(M)):
    print("Yes")
else:
    print("No") 