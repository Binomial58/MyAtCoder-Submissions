H,W=map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
C=0
def DFS(x,y,seen):
    global C
    if S[y][x]in seen:
        return
    seen.add(S[y][x])
    if y==H-1 and x ==W-1:
        C+=1
    if y+1<H:
        DFS(x,y+1,seen.copy())
    if x+1<W:
        DFS(x+1,y,seen.copy())
DFS(0,0,set())
print(C)