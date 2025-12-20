n = int(input())
A = list(map(int, input().split()))
an = 0
a2 = 0
a4 = 0
for a in A:
    if a % 4 == 0:
        a4 += 1
    elif a % 2 == 0:
        a2 += 1
    else:
        an += 1
if a2 == 0:
    if a4 + 1 >= an:
        print("Yes")
    else:
        print("No")
else:
    if a4 >= an:
        print("Yes")
    else:
        print("No")
# print(a4, a2, an)
