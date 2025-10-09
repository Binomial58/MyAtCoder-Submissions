from collections import deque
q=int(input())
L=deque()
R=[]
for i in range(q):
    Q=list(map(str, input().split()))
    if Q[0]=="1":
        L.append(Q[1])
    elif Q[0]=="2":
        R.append(L[-1])
    else:
        L.pop()
for r in R:
    print(r)