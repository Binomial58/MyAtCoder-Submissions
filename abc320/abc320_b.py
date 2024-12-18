S=input()
N=len(S)
maxn=1
for n in range(2,N+1):
    for i in range(N-n+1):
        k=0
        for j in range(i,i+n):
            #右と左に対応する文字を比較
            if S[j]!=S[2*i+n-j-1]:
                k+=1
        if k==0:
            maxn=max(maxn,n)   
print(maxn)