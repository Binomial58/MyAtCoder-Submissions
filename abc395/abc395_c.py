N=int(input())
A=list(map(int, input().split()))
I=[i for i in range(N)]
A,I= zip(*sorted(zip(A, I)))
B=list(set(A))
M=10**10
for i in range(N-1):
    if A[i]==A[i+1]:
        M=min(M,I[i+1]-I[i]+1)
if M==10**10:
    print(-1)
else:
    print(M)