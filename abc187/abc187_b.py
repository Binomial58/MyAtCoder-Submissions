N=int(input())
C=0
Z=[]
for _ in range(N):
    z=list(map(int, input().split()))
    Z.append(z)
for a in range(N):
    for b in range(N):
        if a>=b:
            continue
        else:
            if -1<=(Z[a][1]-Z[b][1])/(Z[a][0]-Z[b][0])<=1:
                C+=1
print(C)