n = int(input())
A = list(map(int, input().split()))
# インデックスと数字が一致しているもの
C = set()
for i in range(n):
    A[i] -= 1
    if A[i] == i:
        C.add(i)
# 一致しているものが出てきた個数
now = -1
count = 0
for i in range(n):
    a = A[i]
    if i in C:
        now += 1
        count += now
    else:
        if i < a and A[a] == i:
            count += 1
    # print(count)
print(count)
