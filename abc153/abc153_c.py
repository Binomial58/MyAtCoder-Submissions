N,K=map(int, input().split())
H=list(map(int, input().split()))
H=sorted(H)
if N<=K:
    print(0)
else:
    print(sum(H[:N-K]))