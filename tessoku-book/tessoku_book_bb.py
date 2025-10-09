q=int(input())
G=dict()
R=[]
for i in range(q):
    Q=list(map(str, input().split()))
    if Q[0]=="1":
        G[Q[1]]=Q[2]
    else:
        R.append(G[Q[1]])
for r in R:
    print(r)