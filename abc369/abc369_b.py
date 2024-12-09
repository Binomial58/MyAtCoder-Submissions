N=int(input())
L=[]
R=[]
S_L=0
S_R=0
for i in range(N):
    A,S=input().split()
    A=int(A)
    if S=="L":
        L.append(A)
    else:
        R.append(A)
for k in range(1,len(L)):
    S_L+=abs(L[k]-L[k-1])
for l in range(1,len(R)):
    S_R+=abs(R[l]-R[l-1])
print(S_R+S_L)