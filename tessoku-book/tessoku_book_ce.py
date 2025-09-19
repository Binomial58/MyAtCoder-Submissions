n=int(input())
A=list(map(int, input().split()))
q=int(input())
R=[]
W=[0]
L=[0]
for i in range(n):
    if A[i]==1:
        W.append(W[i]+1)
        L.append(L[i])
    else:
        W.append(W[i])
        L.append(L[i]+1)
for i in range(q):
    l,r=map(int, input().split())
    w=W[r]-W[l-1]
    l=L[r]-L[l-1]
    if w>l:
        R.append("win")
    elif w==l:
        R.append("draw")
    else:
        R.append("lose")
for r in R:
    print(r)