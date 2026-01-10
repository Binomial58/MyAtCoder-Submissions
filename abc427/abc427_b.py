n = int(input())
A = [1]
for i in range(n):
    now = 0
    for a in A:
        for j in range(len(str(a))):
            now += int(str(a)[j])
    A.append(now)
print(A[-1])
