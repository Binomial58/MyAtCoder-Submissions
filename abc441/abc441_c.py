n, k, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
# 酒が入っていない個数
d = n - k
# print(d)
now = 0
count = d
while now < x and count != n:
    # print(count)
    now += A[count]
    count += 1
    # print(now, count)
if now >= x:
    print(count)
else:
    print(-1)
# print(count)
