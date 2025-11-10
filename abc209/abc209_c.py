n = int(input())
C = list(map(int, input().split()))
C.sort()
r = 1
for i in range(n):
    r *= max(0, C[i] - i)
    r %= 10**9 + 7
print(r)
