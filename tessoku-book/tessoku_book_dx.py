from collections import deque
s=input()
L=deque()
R=[]
for i in range(len(s)):
    if s[i]=="(":
        L.append(i+1)
    else:
        R.append([L.pop(),i+1])
for A in R:
    print(*A)