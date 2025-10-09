from collections import deque
R=[]
L=deque()
q=int(input())
for i in range(q):
    Q=list(map(str, input().split()))
    if Q[0]=="1":
        L.append(Q[1])
    elif Q[0]=="2":
        R.append(L[0])
    else:
        L.popleft()
for r in R:
    print(r)