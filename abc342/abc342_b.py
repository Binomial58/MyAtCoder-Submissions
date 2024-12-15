N=int(input())
P=list(map(int, input().split()))
Q=int(input())
C=[list(map(int, input().split())) for _ in range(Q)]
for i in range(Q):
    if P.index(C[i][0])>P.index(C[i][1]):
        print(C[i][1])
    else:
        print(C[i][0])