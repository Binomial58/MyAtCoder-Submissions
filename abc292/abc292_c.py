n = int(input())
D = [0 for i in range(n - 1)]
for i in range(1, n):
    # print(i)
    j = 1
    while j * j <= i:
        # print(j)
        if i % j == 0:
            p = i // j
            if p == j:
                D[i - 1] += 1
            else:
                D[i - 1] += 2
        j += 1
count = 0
for l in range(len(D)):
    # print(l, len(D) - 1 - l)
    # print(D[l] * D[len(D) - 1 - l])
    count += D[l] * D[len(D) - 1 - l]
print(count)
