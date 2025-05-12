N,A,B=map(int, input().split())
S=[["*"]*(N*B) for i in range(N*A)]
a=0
b=0
for i in range(N*A):
    for j in range(N*B):
        a=i//A
        b=j//B
        if (a+b)%2==0:
            S[i][j]="."
        else:
            S[i][j]="#"
for s in S:
    print("".join(s))
#周期性でタイルの色を管理して出力する．