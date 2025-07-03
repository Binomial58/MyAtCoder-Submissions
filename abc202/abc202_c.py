import collections
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
D=[]
for i in range(N):
    D.append(B[C[i]-1])
X=collections.Counter(A)
Y=collections.Counter(D)
E=list(set(A))
S=0
for i in E:
    S+=X[i]*Y[i]
print(S)