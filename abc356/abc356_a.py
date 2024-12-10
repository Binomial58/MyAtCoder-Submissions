import copy

N,L,R=map(int, input().split())
A=[]
B=[]
p=0
for i in range(1,N+1):
    A.append(i)
for k in range(R,L-1,-1):
    B.append(k)
for j in range(L-1,R):
    A[j]=B[p]
    p+=1
print(*A)