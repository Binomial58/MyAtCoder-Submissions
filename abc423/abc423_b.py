n = int(input())
L = list(map(int, input().split()))
left = 0
right = 0
if 1 in L:
    left = L.index(1)
    right = n - L[::-1].index(1) - 1
print(right - left)
