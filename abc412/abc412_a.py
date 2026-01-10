n = int(input())
count = 0
for i in range(n):
    a, b = map(int, input().split())
    if b > a:
        count += 1
print(count)
