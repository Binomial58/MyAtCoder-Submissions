from collections import deque

S = input()
Q = deque()
S = S[::-1]
for s in S:
    if len(Q) != 0 and s == "W" and Q[-1] == "A":
        Q.pop()
        Q.append("C")
        Q.append("A")
    else:
        Q.append(s)
Q = list(Q)
Q = Q[::-1]
print("".join(Q))
