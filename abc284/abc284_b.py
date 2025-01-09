T=int(input())
B=[]
for _ in range(T):
    count=0
    N=int(input())
    A=list(map(int, input().split()))
    for i in range(N):
        if A[i]%2==1:
            count+=1
    B.append(count)
for j in range(T):
    print(B[j])