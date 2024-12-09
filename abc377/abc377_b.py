#for文として配列を次々に追加していく．
C=[]
for _ in range(8):
    S=input().split()
    C.append("".join(S))
#Cの各要素をリスト化する．
C=[list(row) for row in C]

#外側のループ
for i in range(8):
    for j in range(8):
        #駒があった場合の判定
        if C[i][j]=="#":
            for k in range(8):
                if C[k][j]==".":
                    C[k][j]="x"
            for l in range(8):
                if C[i][l]==".":
                   C[i][l]="x"
T=str(C)
#リストを文字列に変換
S=T.count(".")
print(S)