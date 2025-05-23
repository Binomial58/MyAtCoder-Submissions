N=int(input())
P=list(map(int, input().split()))
S=N
for j in range(N-1):
    S=P[S-2]
    if S==1:
        print(j+1)
        exit()