H,W=map(int, input().split())
C=[list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j]==".":
            used=set()
            for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
                ni,nj=i+dy,j+dx
                if 0<=ni<H and 0<=nj<W:
                    used.add(C[ni][nj])
                for color in "12345":
                    if color not in used:
                        C[i][j]=color
                        break
for row in C:
    print("".join(row))