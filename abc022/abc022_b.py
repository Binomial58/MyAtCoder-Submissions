n = int(input())
count = 0
A = set()
for i in range(n):
    a = int(input())
    if a in A:
        count += 1
    A.add(a)
print(count)
