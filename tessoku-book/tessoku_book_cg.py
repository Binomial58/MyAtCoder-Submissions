n=int(input())
X=[[0 for i in range(1500)]for j in range(1500)]
for i in range(n):
    x,y=map(int, input().split())
    X[y-1][x-1]+=1
Xsum=[[] for i in range(1500)]
for i in range(1500):
    Xsum[i].append(X[i][0])
    for j in range(1499):
        Xsum[i].append(Xsum[i][j]+X[i][j+1])
for j in range(1500):
    for i in range(1499):
        Xsum[i+1][j]+=Xsum[i][j]
Xsum=[[0 for i in range(1500)],*Xsum]
for i in range(1501):
    Xsum[i]=[0,*Xsum[i]]
q=int(input())
R=[]
for i in range(q):
    a,b,c,d=map(int, input().split())
    R.append(Xsum[d][c]-Xsum[d][a-1]-Xsum[b-1][c]+Xsum[b-1][a-1])
for r in R:
    print(r)