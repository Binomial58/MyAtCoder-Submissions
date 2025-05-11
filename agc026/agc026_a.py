N=int(input())
A=list(map(int, input().split()))
C=0
for i in range(N-1):
    if A[i]==A[i+1]:
        C+=1
        A[i+1]=-i
print(C)