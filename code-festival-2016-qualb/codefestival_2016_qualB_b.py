n, a, b = map(int, input().split())
s = input()
sum = 0
sumb = 0
for t in s:
    if t == "a" and sum < a + b:
        print("Yes")
        sum += 1
    elif t == "b" and sum < a + b and sumb < b:
        print("Yes")
        sum += 1
        sumb += 1
    else:
        print("No")
