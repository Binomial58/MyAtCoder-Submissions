N,D=map(int,input().split())
S=input()
Q=list(S)
for i in range(len(Q)-1,-1,-1):
    if (Q[i]=="@")and(D!=0):
        Q[i]="."
        D-=1
strQ="".join(Q)
print(strQ)