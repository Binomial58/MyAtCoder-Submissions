from collections import deque
n=int(input())
A=list(map(int, input().split()))
L=deque()
R=[-1]
L.append([1,A[0]])
for i in range(1,n):
    while len(L)!=0 and L[-1][1]<A[i]:
        L.pop()
    if len(L)==0:
        R.append(-1)
    else:
        R.append(L[-1][0])
    L.append([i+1,A[i]])
print(*R)