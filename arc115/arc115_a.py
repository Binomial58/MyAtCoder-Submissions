n, m = map(int, input().split())
C = [0, 0]
for i in range(n):
    s = input()
    if s.count("1") % 2 == 0:
        C[0] += 1
    else:
        C[1] += 1
print(C[0] * C[1])
