N=int(input())
S=input()
if S.count("T")>S.count("A"):
    print("T")
elif S.count("T")<S.count("A"):
    print("A")
elif S[-1]=="T":
    print("A")
else:
    print("T")