from collections import deque

q = int(input())
Q = deque()
r = 0
l = 0
R = []
flag = True
now = 0
for i in range(q):
    query = list(map(str, input().split()))
    # print(query)
    if query[0] == "1":
        if query[1] == ")":
            r += 1
        else:
            l += 1
        if r > l and query[1] == ")":
            Q.append("]")
            flag = False
            now += 1
        else:
            Q.append(query[1])
    else:
        d = Q.pop()
        if d == ")":
            r -= 1
        elif d == "(":
            l -= 1
        else:
            r -= 1
            now -= 1
            if now == 0:
                flag = True
    if r == l and flag:
        R.append("Yes")
    else:
        R.append("No")
    # print(Q, flag)
    # print(R[-1])
for r in R:
    print(r)
