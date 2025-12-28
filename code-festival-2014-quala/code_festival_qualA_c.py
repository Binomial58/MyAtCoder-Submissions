a, b = map(int, input().split())
bc = b // 4 - b // 100 + b // 400
ac = (a - 1) // 4 - (a - 1) // 100 + (a - 1) // 400
print(bc - ac)
