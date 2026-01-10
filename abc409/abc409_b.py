import bisect

n = int(input())
A = list(map(int, input().split()))
left = 0
right = 10**10
while left < right:
    mid = (left + right) // 2
    count = 0
    for a in A:
        if a >= mid:
            count += 1
    if count >= mid:
        left = mid + 1
    else:
        right = mid
    # print(left, right)
print(left - 1)
