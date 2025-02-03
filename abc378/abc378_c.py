N=int(input())
A=list(map(int, input().split()))
B=[-1]*N
#lastを連想配列として用意
last={}
for i in range(N):
    #lastの中に名前があるかの確認
    if A[i]in last:
        B[i]=last[A[i]]
    #lastの名前に対応する値を更新
    last[A[i]]=i+1
print(*B)