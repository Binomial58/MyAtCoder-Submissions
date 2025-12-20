from collections import deque

n = int(input())
s = input()
R = deque()
R.append(n)
for i in range(n - 1, -1, -1):
    # print(i)
    if s[i] == "L":
        R.append(i)
    else:
        R.appendleft(i)
print(*R)
