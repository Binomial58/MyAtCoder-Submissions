x, y = map(str, input().split())
V = ["Ocelot", "Serval", "Lynx"]
if V.index(x) >= V.index(y):
    print("Yes")
else:
    print("No")
