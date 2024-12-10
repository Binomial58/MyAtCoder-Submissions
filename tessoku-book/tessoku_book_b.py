N,X=map(int, input().split())
A=list(map(int, input().split()))
C=A.count(X)
if C>0:
    print("Yes")
else:
    print("No")