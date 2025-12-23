n, k = map(int, input().split())
D = dict()
for i in range(1, n + 1):
    D[i] = k
if n % 2 == 0:
    A = [n // 2]
    D[n // 2] -= 1
    for i in range(n, 0, -1):
        for j in range(D[i]):
            A.append(i)
    print(*A)
else:
    A = [(n + 1) // 2 for i in range(k)]
    D[(n + 1) // 2] = 0
    if n != 1:
        N = dict()
        count = 1
        for i in range(1, n + 1):
            if i != (n + 1) // 2:
                N[count] = i
                count += 1
        A.append(N[(n - 1) // 2])
        D[N[(n - 1) // 2]] -= 1
        for i in range(n - 1, 0, -1):
            for j in range(D[N[i]]):
                A.append(N[i])
        # print(N)
    print(*A)
