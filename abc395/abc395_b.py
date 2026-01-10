n = int(input())
S = [["#" for i in range(n)] for j in range(n)]
if n % 2 == 0:
    c = n // 2
else:
    c = n // 2 + 1
# print(c)
for i in range(c):
    # 黒く塗る
    l = i
    r = n - 1 - l
    # print(l, r)
    if i % 2 == 0:
        for j in range(l, r + 1):
            for k in range(l, r + 1):
                S[j][k] = "#"
    else:
        for j in range(l, r + 1):
            for k in range(l, r + 1):
                S[j][k] = "."
for s in S:
    print("".join(s))
