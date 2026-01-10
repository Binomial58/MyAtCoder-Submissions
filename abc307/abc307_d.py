from collections import deque

n = int(input())
s = input()
# カッコだけを入れる
Q = deque()
# 全てを入れる
R = deque()
for t in s:
    if t == "(":
        Q.append(t)
        R.append(t)
    elif t == ")":
        if len(Q) != 0 and Q[-1] == "(":
            Q.pop()
            while R[-1] != "(":
                R.pop()
            R.pop()
        else:
            Q.append(t)
            R.append(t)
    else:
        R.append(t)
print("".join(R))
# print(Q)
