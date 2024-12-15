N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.sort(reverse=False)
C=A+B
C.sort(reverse=False)
k=0
a=0
for j in range(N+M):
    if C[j]==A[a]:
        k+=1
        a+=1
    else:
        k=0
    if k==2 or a==N:
        break
if k==2:
    print("Yes")
else:
    print("No")