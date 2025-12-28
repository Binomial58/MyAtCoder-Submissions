n, k = map(int, input().split())
k = abs(k)
l = 2
r = n * 2
count = 0
i = 2
while k + i <= r:
    a = k + i
    b = i
    dn = n + 1
    if a - 1 >= dn:
        ac = a - 1 - 2 * (a - dn)
    else:
        ac = a - 1
    if b - 1 >= dn:
        bc = b - 1 - 2 * (b - dn)
    else:
        bc = b - 1
    count += ac * bc
    i += 1
print(count)
