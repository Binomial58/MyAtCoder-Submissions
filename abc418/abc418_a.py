n=int(input())
s=input()
if n<3:
    print("No")
else:
    if s[n-3:]=="tea":
        print("Yes")
    else:
        print("No")