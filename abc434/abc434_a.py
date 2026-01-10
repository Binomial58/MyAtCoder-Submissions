w, b = map(int, input().split())
w *= 1000
for i in range(1000000000):
    if i * b > w:
        print(i)
        exit()
