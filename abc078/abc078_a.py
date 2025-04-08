X,Y=map(str, input().split())
Z=["A","B","C","D","E","F"]
if Z.index(X)>Z.index(Y):
    print(">")
elif Z.index(X)<Z.index(Y):
    print("<")
else:
    print("=")