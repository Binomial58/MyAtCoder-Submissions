h1, h2, h3, w1, w2, w3 = map(int, input().split())
# a b c
# d e f
# g h i
count = 0
for a in range(1, 29):
    for b in range(1, 29):
        for d in range(1, 29):
            for e in range(1, 29):
                c = h1 - a - b
                if c <= 0:
                    continue
                f = h2 - d - e
                if f <= 0:
                    continue
                g = w1 - a - d
                if g <= 0:
                    continue
                h = w2 - b - e
                if h <= 0:
                    continue
                i = h3 - g - h
                if i <= 0 or c + f + i != w3:
                    continue
                count += 1
print(count)
