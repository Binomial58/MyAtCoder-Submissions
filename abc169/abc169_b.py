n = int(input())
A = list(map(int, input().split()))
r = 1
A.sort()
for a in A:
    r *= a
    if r > 10 ** (18):
        print(-1)
        exit()
print(r)
