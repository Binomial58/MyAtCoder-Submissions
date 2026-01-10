n, s, k = map(int, input().split())
count = 0
for i in range(n):
    p, q = map(int, input().split())
    count += p * q
if count >= s:
    print(count)
else:
    print(count + k)
