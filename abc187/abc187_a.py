def SN (X):
    return int(X[0])+int(X[1])+int(X[2])
A,B=map(str, input().split())
if SN(A)>SN(B):
    print(SN(A))
else:
    print(SN(B))