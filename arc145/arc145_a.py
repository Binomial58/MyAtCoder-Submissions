n = int(input())
S = input()
if (S[0] == "A" and S[-1] == "B") or S == "BA":
    print("No")
else:
    print("Yes")
