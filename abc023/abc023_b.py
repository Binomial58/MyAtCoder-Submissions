from collections import deque

n = int(input())
s = input()
Q = deque()
Q.append("b")
if n % 2 == 0:
    print(-1)
else:
    t = "".join(Q)
    if t == s:
        print(0)
        exit()
    for i in range((n - 1) // 2):
        if i % 3 == 0:
            Q.appendleft("a")
            Q.append("c")
        elif i % 3 == 1:
            Q.appendleft("c")
            Q.append("a")
        else:
            Q.appendleft("b")
            Q.append("b")
        t = "".join(Q)
        if t == s:
            print(i + 1)
            exit()
    print(-1)
