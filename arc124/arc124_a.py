N,K=map(int, input().split())
R=["?" for i in range(N)]
V=[0 for i in range(N)]
for i in range(1,K+1):
    c,k=map(str, input().split())
    R[int(k)-1]=i
    if c=="R":
        for j in range(int(k)):
            V[j]+=1
    else:
        for j in range(int(k),N):
            V[j]+=1
s=1
for i in range(N):
    if R[i]=="?":
        s*=V[i]
s%=998244353
print(s)
