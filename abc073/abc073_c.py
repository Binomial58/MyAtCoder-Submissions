n = int(input())
R = set()
for i in range(n):
    a = int(input())
    if a not in R:
        R.add(a)
    else:
        R.remove(a)
print(len(R))
