from collections import deque

n, m, k = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
H.sort()
H = deque(H)
B.sort(reverse=True)
B = B[:k]
B.sort()
B = deque(B)
for i in range(k):
    b = B.popleft()
    while True:
        h = H.popleft()
        if b >= h:
            break
        if len(H) == 0:
            print("No")
            exit()
    # print(H)
    # print("hogegege", j, H[j - 1])
#     print(b)
# print(H)
# print(B)
print("Yes")
