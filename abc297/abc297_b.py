S=input()
if S.index("B")%2 == S.rindex("B")%2:
    print("No")
    exit()
if S.index("R")<S.index("K")<S.rindex("R"):
    print("Yes")
else:
    print("No")