N=int(input())
A=list(map(int,input().split()))
B=0
C=0
#配列を降順にソート
A.sort(reverse=True)
if N%2==1:
    A.append(0)
    N=N+1
for i in range(0,N-1,2):
    B+=A[i]
for i in range(1,N,2):
    C+=A[i]
D=B-C
print(D)