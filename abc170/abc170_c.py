import copy 
X,N=map(int, input().split())
P=set(map(int, input().split()))
R={i for i in range(-1,150)}
Y=list(R-P)
Z=copy.deepcopy(Y)
for i in range(len(Z)):
    Z[i]=abs(Z[i]-X)
print(Y[Z.index(min(Z))])