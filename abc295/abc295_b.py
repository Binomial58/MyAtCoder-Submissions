#マンハッタン距離関数の定義
def manhattan(x,y,a,b) :
    return abs(x-a)+abs(y-b)

R,C=map(int, input().split())
B=[]
for t in range(R):
    B.append(list(input()))
for c in range(C):
    for r in range(R):
        if B[r][c]!="." and B[r][c]!="#":
            for x in range(C):
                for y in range(R):
                    if manhattan(c,r,x,y)<=int(B[r][c]) and (B[y][x]=="." or B[y][x]=="#"):
                        B[y][x]="."
            B[r][c]="."
for t in range(R):
    print("".join(B[t]))