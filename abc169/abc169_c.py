a, b = map(str, input().split())
a = int(a)
B = []
for i in b:
    if i != ".":
        B.append(i)
b = int("".join(B))
# print(a, b)
print((a * b) // 100)
