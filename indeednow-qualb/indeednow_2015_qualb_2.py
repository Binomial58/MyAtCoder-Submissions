from collections import deque

s = input()
t = input()
S = [s[i] for i in range(len(s))]
T = [t[i] for i in range(len(t))]
S = deque(S)
T = deque(T)
if len(s) != len(t):
    print(-1)
else:
    count = 0
    while S != T:
        a = S.pop()
        S.appendleft(a)
        count += 1
        if count == len(s):
            print(-1)
            exit()
    print(count)