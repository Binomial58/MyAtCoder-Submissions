N=int(input())
A=list(map(int, input().split()))
B=[]
for i in range(N-1):
    if A[i]<A[i+1]:
        for k in range(A[i],A[i+1]):
            B.append(k)
    else:
        for k in range(A[i],A[i+1],-1):
            B.append(k)
if B[-1]<A[N-1]:
    for j in range(B[-1]+1,A[N-1]+1):
        B.append(j)
else:
    for j in range(B[-1]-1,A[N-1]-1,-1):
        B.append(j)
print(*B)