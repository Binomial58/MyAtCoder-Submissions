N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=[A[0]*B[0]]
D=[A[0]]
for i in range(1,N):
    if D[-1]<=A[i]:
        D.append(A[i])
    else:
        D.append(D[-1])
for j in range(1,N):
    C.append(max(C[-1],B[j]*D[j]))
for c in C:
    print(c)