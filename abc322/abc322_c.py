N,M=map(int, input().split())
A=list(map(int, input().split()))
k=0
for n in range(1,N+1):
    m=A[k]
    if n>m:
        k+=1
        m=A[k]
    print(m-n)