a, b, c, d = map(int, input().split())
if a < c:
    print("No")
elif a > c:
    print("Yes")
else:
    if b > d:
        print("Yes")
    else:
        print("No")
