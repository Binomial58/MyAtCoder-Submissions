X=["Ocelot","Serval","Lynx"]
x,y=map(str, input().split())
if X.index(x)>=X.index(y):
    print("Yes")
else:
    print("No")
