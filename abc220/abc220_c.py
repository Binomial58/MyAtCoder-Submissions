N=int(input())
A=list(map(int, input().split()))
X=int(input())
c=0
S=0
c+=N*(X//sum(A))
S+=sum(A)*(X//sum(A))
while S<=X:
    S+=A[c%N]
    c+=1
print(c) 