a, b, c = map(int, input().split())
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print(0)
else:
    A = [a, b, c]
    A.sort()
    print(A[0] * A[1])
