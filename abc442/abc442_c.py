n,m=map(int, input().split())
V=[n-1 for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    V[a-1]-=1
    V[b-1]-=1
R=[]
for i in range(n):
    if V[i]<3:
        R.append(0)
    else:
        v=V[i]
        R.append((v*(v-1)*(v-2))//6)
print(*R)
