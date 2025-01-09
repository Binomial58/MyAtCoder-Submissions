N,M=map(int, input().split())
S=[input() for _ in range(N)]
C=0
for a in range(N):
    for b in range(N):
        count=0
        if a>=b:
            continue
        for i in range(M):
            if S[a][i]=="o" or S[b][i]=="o":
                count+=1
        if count==M:
            C+=1
print(C)