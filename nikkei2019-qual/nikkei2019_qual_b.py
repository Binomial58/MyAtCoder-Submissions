N=int(input())
A=input()
B=input()
C=input()
T=0
for i in range(N):
    T+=len(set([A[i],B[i],C[i]]))-1
print(T)