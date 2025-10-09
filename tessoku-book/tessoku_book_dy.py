from collections import deque
n,x=map(int, input().split())
A=list(input())
L=deque()
L.append(x)
while len(L)!=0:
    pos=L[0]
    L.popleft()
    A[pos-1]="@"
    if pos>=2 and A[pos-2]==".":
        A[pos-2]="@"
        L.append(pos-1)
    if pos<=n-1 and A[pos]==".":
        A[pos]="@"
        L.append(pos+1)
print("".join(A))