from collections import deque
Q=int(input())
W=deque()
R=[]
for i in range(Q):
    S=0
    q=list(map(int, input().split()))
    if q[0]==1:
        c=q[1]
        x=q[2]
        W.append([c,x])
    else:
        k=q[1]
        while k>0:
            if k<=W[0][0]:
                S+=k*W[0][1]
                W[0][0]-=k
                k=0
                if W[0][0]==0:
                    W.popleft()
            else:
                S+=W[0][0]*W[0][1]
                k-=W[0][0]
                W.popleft()
        R.append(S)
for r in R:
    print(r)
