a, b = map(int, input().split())
x = int(a / b)
A = [abs(a / b - (x - 1)), abs(a / b - x), abs(a / b - (x + 1))]
i = A.index(min(A))
print(x - 1 + i)
