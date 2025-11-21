n = int(input())
count = max(n - 2, 0)
for j in range(2, n):
    i = 2
    while i * i <= j:
        if j % i == 0:
            count -= 1
            break
        i += 1
print(count)
