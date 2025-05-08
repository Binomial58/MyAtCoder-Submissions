X=list(map(int, input().split()))
K=int(input())
for i in range(K):
    if X[1]<=X[0]:
        X[1]*=2
    elif X[2]<=X[1]:
        X[2]*=2
if X[0]<X[1]<X[2]:
    print("Yes")
else:
    print("No")