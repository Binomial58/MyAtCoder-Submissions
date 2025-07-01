N,K=map(int, input().split())
A=[0]
B=[0]
j=0
for i in range(N):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)
A,B= zip(*sorted(zip(A, B)))
for k in range(N):
    d=A[k+1]-A[k]
    if K>=d:
        K=K-d+B[k+1]
        j=A[k+1]
    else:
        j+=K
        K=0
        break
j+=K
K=0
print(j)