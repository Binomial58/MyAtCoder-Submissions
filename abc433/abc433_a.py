x, y, z = map(int, input().split())
for i in range(1000):
    if x / y == z:
        print("Yes")
        exit()
    x += 1
    y += 1
print("No")
