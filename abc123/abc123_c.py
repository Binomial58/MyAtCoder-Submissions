n = int(input())
m = 10**20
for i in range(5):
    m = min(m, int(input()))
print(4 + (n + m - 1) // m)
# print(m)
