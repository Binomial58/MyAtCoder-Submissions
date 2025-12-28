n = input()
now = 0
for i in range(len(n) - 1):
    # print("9" * i)
    d = int("9" * (i + 1)) - 10 ** (i) + 1
    now += d * (d + 1) // 2
    now %= 998244353
e = int(n) - 10 ** (len(n) - 1) + 1
now += e * (e + 1) // 2
now %= 998244353
print(now)
