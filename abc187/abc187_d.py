n = int(input())
sa = 0
T = []
for i in range(n):
    a, b = map(int, input().split())
    T.append([a, a + b, 2 * a + b])
    sa += a
T = sorted(T, reverse=True, key=lambda x: (x[2]))
# print(sa)
# print(T)
count = 0
now = 0
while now <= sa:
    now += T[count][1]
    sa -= T[count][0]
    count += 1
print(count)
