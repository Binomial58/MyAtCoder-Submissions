n,k=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))
D=list(map(int, input().split()))
P=[]
Q=set()
for i in range(n):
    for j in range(n):
        P.append(A[i]+B[j])
for i in range(n):
    for j in range(n):
        Q.add(C[i]+D[j])
for p in P:
    d=k-p
    if d in Q:
        print("Yes")
        exit()
print("No")
