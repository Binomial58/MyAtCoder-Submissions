N=int(input())
#賭けた番号の管理
A=[]
#それぞれの人が賭けた個数の管理
M=[]
#当たった人の管理
D=[]
for _ in range(N):
    C=int(input())
    B=list(map(int, input().split()))
    A.append(B)
    M.append(len(B))
X=int(input())
for i in range(N):
    if A[i].count(X)==1:
        D.append(i)
K=[M[k] for k in D]
if len(D)==0:
    print(0)
    exit()
K,D=zip(*sorted(zip(K,D)))
R=[D[t]+1 for t in range(len(D))]
min=K.count(min(K))
print(len(R[:min]))
print(*R[:min])