A,B,K=map(int, input().split())
X=[i for i in range(A,min(B,A+K))]
Y=[i for i in range(max(A,B-K+1),B+1)]
Z=list(set(X+Y))
Z.sort()
for z in Z:
    print(z)
