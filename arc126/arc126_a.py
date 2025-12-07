t = int(input())
R = []
for i in range(t):
    a, b, c = map(int, input().split())
    b //= 2
    # a:2の本数 b:6の本数 c:4の本数
    # print(a, c, b)
    count = 0
    # 6と4を組み合わせ
    d = min(c, b)
    count += d
    c -= d
    b -= d
    # print(a, c, b)
    # 6と2を組み合わせ
    d = min(a // 2, b)
    count += d
    a -= d * 2
    b -= d
    # print(a, c, b)
    # 4と2の組み合わせ
    # 2+4*2
    d = min(a, c // 2)
    count += d
    a -= d
    c -= d * 2
    d = min(a // 3, c)
    count += d
    a -= d * 3
    c -= d
    count += a // 5
    R.append(count)
for r in R:
    print(r)
