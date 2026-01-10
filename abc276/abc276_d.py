import math

n = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
Ag = math.gcd(A[0], A[1])
for i in range(2, n):
    Ag = math.gcd(Ag, A[i])
# print(Ag)
for i in range(n):
    if A[i] % Ag != 0:
        print(-1)
        exit()
    else:
        d = A[i] // Ag
        # print(d)
        while d % 2 == 0:
            d //= 2
            count += 1
        while d % 3 == 0:
            d //= 3
            count += 1
        if d != 1:
            print(-1)
            exit()
        A[i] = Ag
print(count)
