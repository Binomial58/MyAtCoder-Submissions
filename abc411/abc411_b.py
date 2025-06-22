N=int(input())
D=list(map(int, input().split()))
R=[0]
for i in range(N-1):
    R.append(R[-1]+D[i])
for i in range(N-1):
    E=[]
    for j in range(N):
        if j>i:
            E.append(R[j]-R[i])
    print(*E)