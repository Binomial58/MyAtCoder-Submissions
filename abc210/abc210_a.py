N,A,X,Y=map(int, input().split())
if A<N:
    print(A*X+(N-A)*Y)
else:
    print(N*X)