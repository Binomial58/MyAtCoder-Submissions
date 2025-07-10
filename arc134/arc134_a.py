n,l,w=map(int, input().split())
A=list(map(int, input().split()))
R=[]
L=[]
T=[]
s=0
for i in range(n):
    L.append(A[i])
    R.append(A[i]+w)
T.append(L[0])
for j in range(n-1):
    if R[j]<L[j+1]:
        T.append(L[j+1]-R[j])
T.append(l-R[-1])
for t in T:
    s+=(t-1)//w+1
print(s)