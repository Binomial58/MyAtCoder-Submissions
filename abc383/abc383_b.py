import copy

def manhattan(x,y,a,b) :
    return abs(x-a)+abs(y-b)

H,W,D=map(int, input().split())
S=[]

maxS=0

for k in range(H):
    #1行をリストとして格納
    S.append(list(input()))
for j_1 in range(H):
    for i_1 in range(W):
        if S[j_1][i_1]!=".":
            #ループの先頭に戻る
            continue
        for j_2 in range(H):
            for i_2 in range(W):
                if S[j_2][i_2]!=S[j_1][i_1] and S[j_2][i_2]!=".":
                    continue
                T=copy.deepcopy(S)
                for x in range(H):
                    for y in range(W):
                        if manhattan(x,y,j_1,i_1)<=D or manhattan(x,y,j_2,i_2)<=D:
                            if T[x][y]==".":
                                T[x][y]="o"
                #oの個数のカウント
                countf=sum(row.count("o")for row in T)
                maxS=max(maxS,countf)
print(maxS)