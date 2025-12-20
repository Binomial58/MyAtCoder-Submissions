n = int(input())
A = list(map(int, input().split()))
C = [0 for i in range(8)]
count = 0
for a in A:
    if a // 400 < 8:
        C[a // 400] += 1
    else:
        count += 1
print(max(8 - C.count(0), 1), 8 - C.count(0) + count)
