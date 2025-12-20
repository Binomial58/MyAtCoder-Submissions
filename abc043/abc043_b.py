from collections import deque

s = input()
S = deque()
for t in s:
    if t == "B":
        if len(S) != 0:
            S.pop()
    else:
        S.append(t)
print("".join(S))
