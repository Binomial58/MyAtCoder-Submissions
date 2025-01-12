N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.append(B[-1]+2)
B.append(A[-2]+2)
D=[]
E=[]
C=A+B
C.sort()
a=0
b=0
for i in range(N+M):
    if A[a]<B[b]:
        D.append(i+1)
        a+=1
    else:
        E.append(i+1)
        b+=1
print(*D)
print(*E)