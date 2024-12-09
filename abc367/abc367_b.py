X=float(input())
X=str(X)
L=len(X)
while X[L-1]=="0":
    X=X.rstrip()
    L-=1
L=len(X)
if X.count(".0")==1:
    X=X.rstrip("0")
    X=X.rstrip(".")
print(X)