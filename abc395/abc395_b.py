N=int(input())
#深いコピーにする
S=[[""]*N for _ in range(N)]
for i in range(N):
    R=N-i
    if i%2==0:
        for j in range(i,R):
            for k in range(i,R):
                S[j][k]="#"
    else:
        for j in range(i,R):
            for k in range(i,R):
                S[j][k]="."
for i in range(N):
    print("".join(S[i]))