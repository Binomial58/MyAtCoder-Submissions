n = int(input())
S = [-1 for i in range(n)]
S[0] = 0
S[-1] = 1
left = 0
right = n - 1
while left < right:
    mid = (left + right) // 2
    print("?", mid + 1)
    s = int(input())
    S[mid] = s
    if s == 0:
        left = mid + 1
    else:
        right = mid
    # print(S)
    # print(left, right)
print("!", left)
