n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
Ans = [["." for i in range(s - r + 1)] for i in range(q - p + 1)]
for i in range(p, q + 1):
    for j in range(r, s + 1):
        # print(i, j)
        # print(i - a, j - b)
        if i - a == j - b:
            Ans[i - p][j - r] = "#"
        elif i - a == -(j - b):
            Ans[i - p][j - r] = "#"
        # print(i - a, j - b)
# print(Ans)
for a in Ans:
    print("".join(a))
