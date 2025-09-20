n,k=map(int, input().split())
A=list(map(int, input().split()))
B=A[:n//2]
C=A[n//2:]
nb=len(B)
sumB=set()
nc=len(C)
sumC=set()
for i in range(1<<nb):
    s=0
    for j in range(nb):
        if (i>>j) & 1:
            s+=B[j]
    sumB.add(s)
for i in range(1<<nc):
    s=0
    for j in range(nc):
        if (i>>j) & 1:
            s+=C[j]
    sumC.add(s)
sumC=list(sumC)
for c in sumC:
    d=k-c
    if d in sumB:
        print("Yes")
        exit()
print("No")