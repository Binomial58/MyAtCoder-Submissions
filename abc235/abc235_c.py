n,q=map(int, input().split())
A=list(map(int, input().split()))
B={}
R=[]
for i in range(n):
    if A[i] not in B:
        B[A[i]]=[i+1]
    else:
        B[A[i]].append(i+1)
for i in range(q):
    x,k=map(int, input().split())
    if x in B and len(B[x])>=k:
        R.append(B[x][k-1])
    else:
        R.append(-1)
for r in R:
    print(r)