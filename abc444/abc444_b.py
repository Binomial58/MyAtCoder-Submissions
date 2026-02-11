n, k = map(int, input().split())
count = 0
# print(n, k)
for i in range(1, n + 1):
    # print(i)
    s = str(i)
    now = 0
    for j in range(len(s)):
        now += int(s[j])
    if now == k:
        count += 1
print(count)
