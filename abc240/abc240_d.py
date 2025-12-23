from collections import deque

n = int(input())
A = list(map(int, input().split()))
Q = deque()
count = 0
for i in range(n):
    if len(Q) == 0 or Q[-1][0] != A[i]:
        Q.append([A[i], 1])
        count += 1
    elif Q[-1][0] == A[i]:
        if Q[-1][1] + 1 == A[i]:
            Q.pop()
            count -= A[i] - 1
        else:
            Q[-1][1] += 1
            count += 1
    print(count)
