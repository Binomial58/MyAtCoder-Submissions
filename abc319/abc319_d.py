def can(mid):
    count = 1
    now = 0
    for i in range(n):
        if L[i] > mid:
            return False
        if now == 0:
            now = L[i]
        else:
            if now + L[i] + 1 <= mid:
                now += L[i] + 1
            else:
                now = L[i]
                count += 1
    if count <= m:
        return True
    else:
        return False


n, m = map(int, input().split())
L = list(map(int, input().split()))
left = 0
right = 10**16
mid = (left + right) // 2
while left < right:
    if can(mid):
        right = mid
    else:
        left = mid + 1
    mid = (left + right) // 2
    # print(left, right)
print(left)
