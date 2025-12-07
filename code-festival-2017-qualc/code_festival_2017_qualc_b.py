n = int(input())
A = list(map(int, input().split()))
all = 3**n
now = 1
for a in A:
    if a % 2 == 0:
        now *= 2
print(all - now)
