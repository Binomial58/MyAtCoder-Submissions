from collections import deque

s = list(input())
q = int(input())
S = deque(s)
Rev = False
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == "1":
        Rev = not Rev
    else:
        if query[1] == "1":
            if Rev:
                S.append(query[2])
            else:
                S.appendleft(query[2])
        else:
            if Rev:
                S.appendleft(query[2])
            else:
                S.append(query[2])
t = "".join(S)
if Rev:
    print(t[::-1])
else:
    print(t)
# print("".join(S))
