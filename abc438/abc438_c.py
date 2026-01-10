from collections import deque

n = int(input())
A = list(map(int, input().split()))
Q = deque()
now = 0
for i in range(n):
    if len(Q) == 0 or Q[-1][0] != A[i]:
        Q.append([A[i], 1])
        now += 1
    else:
        # print(Q[-1][1])
        if Q[-1][1] != 3:
            Q[-1][1] += 1
            now += 1
        else:
            Q.pop()
            now -= 3
    # print(Q)
print(now)
