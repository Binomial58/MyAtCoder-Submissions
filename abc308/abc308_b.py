N,M=map(int, input().split())
C=list(map(str, input().split()))
D=list(map(str, input().split()))
P=list(map(int, input().split()))
S=0
for i in range(N):
    if D.count(C[i])==0:
        S+=P[0]
    else:
        S+=P[D.index(C[i])+1]
print(S)