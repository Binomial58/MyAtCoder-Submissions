from collections import deque

s = input()
Q = deque()
for i in s:
    if len(Q) != 0:
        if i != Q[-1]:
            Q.pop()
        else:
            Q.append(i)
    else:
        Q.append(i)
    # print(Q)
print(len(s) - len(Q))
