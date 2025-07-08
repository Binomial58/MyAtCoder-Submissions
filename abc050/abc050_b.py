N=int(input())
T=list(map(int, input().split()))
S=sum(T)
M=int(input())
X=[]
R=[]
for i in range(M):
    p,x=map(int, input().split())
    R.append(S-T[p-1]+x)
for r in R:
    print(r)