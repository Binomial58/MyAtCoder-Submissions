N=int(input())
S=list(map(int, input().split()))
D=0
for i in range(N):
    C=0
    for a in range(1,143):
        for b in range(1,143):
            if S[i]==4*a*b+3*a+3*b:
                C=1
    if C==0:
        D+=1
print(D)