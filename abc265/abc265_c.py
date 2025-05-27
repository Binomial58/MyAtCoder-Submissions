H,W=map(int, input().split())
G=[list(input()) for _ in range(H)]
A=[[0]*W for j in range(H)]
x=0
y=0
A[0][0]=1
while True:
    T=G[y][x]
    if T=="R":
        if x!=W-1:
            x+=1
            A[y][x]+=1
        else:
            print(y+1,x+1)
            exit()
    elif T=="L":
        if x!=0:
            x-=1
            A[y][x]+=1
        else:
            print(y+1,x+1)
            exit()
    elif T=="U":
        if y!=0:
            y-=1
            A[y][x]+=1
        else:
            print(y+1,x+1)
            exit()
    else:
        if y!=H-1:
            y+=1
            A[y][x]+=1
        else:
            print(y+1,x+1)
            exit()
    if A[y][x]==2:
        print(-1)
        exit()