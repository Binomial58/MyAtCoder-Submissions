from collections import deque

n, m, k = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
H.sort()
B.sort()
H = deque(H)
B = deque(B)
count = 0
while len(B) != 0 and count != k:
    h = H.popleft()
    b = B.popleft()
    if h <= b:
        count += 1
    else:
        H.appendleft(h)
if count == k:
    print("Yes")
else:
    print("No")
