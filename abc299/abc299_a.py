N=int(input())
S=input()
a=S.index("|")
b=S.rindex("|")
if a<S.index("*")<b:
    print("in")
else:
    print("out")