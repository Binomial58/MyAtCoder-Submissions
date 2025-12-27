a, b, n = map(int, input().split())
if n + 1 >= b:
    print((a * (b - 1)) // b - a * ((b - 1) // b))
else:
    print((a * n) // b - a * (n // b))
# for i in range(n + 1):
#     print(i, (a * i) // b - a * (i // b))
