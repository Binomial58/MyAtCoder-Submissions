from collections import deque
r,c=map(int, input().split())
S=list(map(int, input().split()))
S[0],S[1]=S[0]-1,S[1]-1
G=list(map(int, input().split()))
G[0],G[1]=G[0]-1,G[1]-1
C=[list(input()) for _ in range(r)]
vec=[[1,0],[-1,0],[0,1],[0,-1]]
isdone=[[False for i in range(c)]for i in range(r)]
time=[[10**9 for i in range(c)]for i in range(r)]
L=deque()
L.append(S)
time[S[0]][S[1]]=0
isdone[S[0]][S[1]]=True
while len(L)!=0:
    now=L.popleft()
    for v in vec:
        y=now[0]+v[0]
        x=now[1]+v[1]
        if C[y][x]==".":
            time[y][x]=min(time[y][x],time[now[0]][now[1]]+1)
            if G!=[y,x] and not isdone[y][x]:
                L.append([y,x])
                isdone[y][x]=True
print(time[G[0]][G[1]])