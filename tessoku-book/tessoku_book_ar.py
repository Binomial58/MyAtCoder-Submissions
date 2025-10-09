n,q=map(int, input().split())
A=[i for i in range(1,n+1)]
R=[]
# now=1で逆順の状態
now=0
for i in range(q):
    Q=list(map(int, input().split()))
    if Q[0]==1:
        if now==0:
            A[Q[1]-1]=Q[2]
        else:
            A[n-Q[1]]=Q[2]
    elif Q[0]==2:
        now=1-now
    else:
        if now==0:
            R.append(A[Q[1]-1])
        else:
            R.append(A[n-Q[1]])
for r in R:
    print(r)
