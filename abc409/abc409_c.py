import collections
N,L=map(int, input().split())
D=list(map(int, input().split()))
S=0
A=[[],[],[]]
if L%3!=0:
    print(0)
    exit()
R=[0]
for i in range(N-1):
    s=(R[-1]+D[i])%(L)
    R.append(s)
R.sort()
for i in range(N):
    if R[i]<L//3:
        A[0].append(R[i]%(L//3))
    elif R[i]<L//3*2:
        A[1].append(R[i]%(L//3))
    else:
        A[2].append(R[i]%(L//3))
X=collections.Counter(A[0])
Y=collections.Counter(A[1])
Z=collections.Counter(A[2])
for i in range(L//3):
    S+=X[i]*Y[i]*Z[i]
print(S)