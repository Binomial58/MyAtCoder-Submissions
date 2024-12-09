N=int(input())
A=list(map(int,input().split()))
C=A.count(0)
d=0
while C<N-1:
    A.sort(reverse=True)
    A[0]-=1
    A[1]-=1
    C=A.count(0)
    d+=1
print(d)