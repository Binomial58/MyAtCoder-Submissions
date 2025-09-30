n=int(input())
X=set(2+i for i in range(n-1))
for i in range(2,max(X)):
    if i in X:
        X-=set(k*i for k in range(2,n//i+100))
X=list(X)
X.sort()
for x in X:
    print(x)