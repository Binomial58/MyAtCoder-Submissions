s=input()
S=["red","blue","green"]
T=["SSS","FFF","MMM"]
if s in S:
    print(T[S.index(s)])
else:
    print("Unknown")