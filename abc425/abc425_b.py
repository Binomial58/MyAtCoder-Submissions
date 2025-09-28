import copy
n=int(input())
A=list(map(int, input().split()))
for i in range(1,n+1):
    if A.count(i)>1:
        print("No")
        exit()
P=copy.deepcopy(A)
B=set(A)
C=set(i for i in range(1,n+1))
C-=B
C=list(C)
j=0
for i in range(n):
    if P[i]==-1:
        P[i]=C[j]
        j+=1
print("Yes")
print(*P)