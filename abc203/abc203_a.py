X=list(map(int, input().split()))
X.sort()
if X[0]==X[1]:
    print(X[2])
elif X[1]==X[2]:
    print(X[0])
else:
    print(0)