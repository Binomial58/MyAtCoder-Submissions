N=int(input())
P=list(map(int, input().split()))
if P[0]!=max(P):
    print(max(P)-P[0]+1)
else:
    if P.count(P[0])!=1:
        print(1)
    else:
        print(0)