N=int(input())
P=list(map(int, input().split()))
M=[P[0]]
C=0
for i in range(1,N):
    if M[-1]<P[i]:
        M.append(M[-1])
    else:
        M.append(P[i])
for i in range(N):
    if M[i]>=P[i]:
        C+=1
print(C)