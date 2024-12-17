N=int(input())
D=list(map(int, input().split()))
#ソロ目の日のカウント
count=0
#ゾロ目の月の集計
eye=[]
for i in range(1,N+1):
    S=str(i)
    L=len(S)
    if S.count(S[0])==L:
        eye.append(i)
for k in eye:
    R=str(k)
    W=int(R[0])
    if D[k-1]>=W:
        count+=1
        if D[k-1]>=W+W*10:
            count+=1
print(count)