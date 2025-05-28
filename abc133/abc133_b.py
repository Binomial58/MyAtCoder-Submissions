N,D=map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
R=[]
C=0
for i in range(N):
    for j in range(N):
        if i>j:
            s=0
            for k in range(D):
                s+=(S[i][k]-S[j][k])**2
            e=0
            while e*e<=s:
                if e*e==s:
                    C+=1
                    break
                e+=1
print(C) 