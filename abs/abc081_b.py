N=int(input())
A=list(map(int,input().split()))
j=0
while all([v%2==0 for v in A]):
    for i in range(N):
        A[i]=A[i]/2
    j+=1
print(j)