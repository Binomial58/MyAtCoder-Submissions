n,q=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
R=[]
s=0
for i in range(n):
    s+=min(A[i],B[i])
for i in range(q):
    query=list(map(str, input().split()))
    x=int(query[1])-1
    v=int(query[2])
    if query[0]=="A":
        s-=min(A[x],B[x])
        A[x]=v
        s+=min(A[x],B[x])
        R.append(s)
    else:
        s-=min(A[x],B[x])
        B[x]=v
        s+=min(A[x],B[x])
        R.append(s)
for r in R:
    print(r)