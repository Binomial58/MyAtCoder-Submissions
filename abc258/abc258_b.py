n = int(input())
vec = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
A = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    a = input()
    for j in range(n):
        A[i][j] = int(a[j])
R = []
for i in range(n):
    for j in range(n):
        for v in vec:
            now = []
            x = i
            y = j
            for k in range(n):
                x += v[1]
                y += v[0]
                x %= n
                y %= n
                now.append(str(A[y][x]))
            # print(now)
            R.append(int("".join(now)))
print(max(R))
