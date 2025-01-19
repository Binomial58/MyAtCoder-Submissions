from collections import deque
Q=int(input())
R=deque()
R.append(0)
S=[]
W=0
E=0
for _ in range(Q):
    t,*x = map(int,input().split())
    if t==1:
        W+=x[0]
        R.append(W)
    if t==2:
        E+=R[1]-R[0]
        R.popleft()
    if t==3:
        X=x[0]
        S.append(R[X-1]-E)
for s in S:
    print(s)