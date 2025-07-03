N,M=map(int, input().split())
S = [list(input()) for _ in range(N)]
R=[]
T=[[0,3],[1,3],[2,3],[3,3],[3,2],[3,1],[3,0]]
for a in range(M-8):
    for b in range(N-8):
        e=0
        for c in range(3):
            for d in range(3):
                if S[b+c][a+d]!="#":
                    e=1
        for c in range(3):
            for d in range(3):
                if S[b+c+6][a+d+6]!="#":
                    e=1
        for k in range(7):
            if S[b+T[k][1]][a+T[k][0]]!=".":
                e=1
        for k in range(7):
            if S[b+8-T[k][1]][a+8-T[k][0]]!=".":
                e=1
        if e==0:
            R.append([b+1,a+1])
R.sort()
for r in R:
    print(*r)