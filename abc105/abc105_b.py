n = int(input())
flag = False
for a in range(50):
    for b in range(50):
        if a * 4 + b * 7 == n:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
