n = int(input())
s = input()
if n < 3:
    print("No")
    exit()
if s[::-1][:3] == "aet":
    print("Yes")
else:
    print("No")
