h,w=map(int, input().split())
X= [list(map(int, input().split())) for _ in range(h)]
Xsum=[[]for j in range(h)]
for i in range(h):
    Xsum[i].append(X[i][0])
    for j in range(w-1):
        Xsum[i].append(Xsum[i][j]+X[i][j+1])
for j in range(w):
    for i in range(h-1):
        Xsum[i+1][j]+=Xsum[i][j]
q=int(input())
R=[]
Xsum=[[0 for i in range(w)],*Xsum]
for i in range(h+1):
    Xsum[i]=[0,*Xsum[i]]
for i in range(q):
    a,b,c,d=map(int, input().split())
    R.append(Xsum[c][d]-Xsum[c][b-1]-Xsum[a-1][d]+Xsum[a-1][b-1])
for r in R:
    print(r)
