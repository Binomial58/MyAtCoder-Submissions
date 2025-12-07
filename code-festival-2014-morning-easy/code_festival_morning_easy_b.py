n = int(input())
n = (n - 1) % 40
n += 1
if n <= 20:
    print(n)
else:
    print(40 - n + 1)
