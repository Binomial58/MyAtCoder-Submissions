N,K=map(int, input().split())
A=list(map(int, input().split()))
B=[]
for i in range(1,N-K+1):
    if A[i-1]<A[K-1+i]:
        print("Yes")
    else:
        print("No")