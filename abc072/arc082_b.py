n = int(input())
P = list(map(int, input().split()))
I = []
for i in range(n):
    if P[i] == i + 1:
        I.append(i)
# print(I)
count = len(I)
for i in range(1, len(I)):
    if I[i - 1] + 1 == I[i]:
        count -= 1
        I[i] = -1
print(count)
