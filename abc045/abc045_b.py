from collections import deque

A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))
now = "a"
while True:
    if now == "a":
        if len(A) == 0:
            print("A")
            exit()
        now = A.popleft()
    elif now == "b":
        if len(B) == 0:
            print("B")
            exit()
        now = B.popleft()
    else:
        if len(C) == 0:
            print("C")
            exit()
        now = C.popleft()
