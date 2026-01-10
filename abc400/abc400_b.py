n, m = map(int, input().split())
count = 0
for i in range(m + 1):
    count += n**i
    if count > 10**9:
        print("inf")
        exit()
print(count)
