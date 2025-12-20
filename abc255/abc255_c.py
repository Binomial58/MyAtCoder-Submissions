x, a, d, n = map(int, input().split())
f = a
e = a + d * (n - 1)
f, e = min(f, e), max(f, e)
# print(f, e)
if f < x < e:
    # 中に入っている処理
    m = (x - f) % d
    print(min(abs(m), abs(d - m)))
else:
    print(min(abs(x - f), abs(x - e)))
