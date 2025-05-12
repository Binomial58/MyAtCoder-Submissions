N,K=map(int, input().split())
for k in range(K):
    N=list(str(N))
    N=sorted(N)
    if N[0]==0:
        A=int("".join(N[1:]))
    else:
        A=int("".join(N))
    N.sort(reverse=True)
    B=int("".join(N))
    N=B-A
print(N)