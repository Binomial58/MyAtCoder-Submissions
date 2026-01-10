def rev(n):
    return int(str(n)[::-1])


x, y = map(int, input().split())
R = [0 for i in range(10)]
R[0] = x
R[1] = y
for i in range(2, 10):
    R[i] = rev(R[i - 1] + R[i - 2])
# print(R)
print(R[-1])
