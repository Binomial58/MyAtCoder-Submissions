q=int(input())
R=[]
X=set(2+i for i in range(300000))
for i in range(2,max(X)):
    if i in X:
        X-=set(k*i for k in range(2,300000//i+100))
for i in range(q):
    x=int(input())
    if x in X:
        R.append("Yes")
    else:
        R.append("No")
for r in R:
    print(r)