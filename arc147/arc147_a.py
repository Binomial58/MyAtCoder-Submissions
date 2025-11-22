from collections import deque

n = int(input())
A = list(map(int, input().split()))
now = min(A)
A.sort(reverse=True)
A = A[: n - 1]
A = deque(A)
count = 0
# print(A, now)
while len(A) != 0:
    d = A.popleft()
    d %= now
    # print(d, now)
    if d != 0:
        A.append(now)
        now = d
    count += 1
    # print(A, now)
print(count)
