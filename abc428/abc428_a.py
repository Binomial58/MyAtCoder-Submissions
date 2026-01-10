s, a, b, x = map(int, input().split())
now = 0
run = 0
for t in range(x):
    if now <= a - 1:
        run += s
    now += 1
    if now == a + b:
        now = 0
print(run)
