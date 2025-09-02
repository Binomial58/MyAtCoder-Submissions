import bisect
import math
n,x=map(int, input().split())
X=list(map(int, input().split()))
X.sort()
dis=[]
for i in range(n-1):
    dis.append(X[i+1]-X[i])
index=bisect.bisect(X,x)
if index==0:
    d=abs(X[index]-x)
elif index==n:
    d=abs(X[index-1]-x)
else:
    d=min(abs(X[index]-x),abs(X[index-1]-x))
if n!=1:
    print(math.gcd(*dis,d))
else:
    print(d)