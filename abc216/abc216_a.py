S=input()
X=S.index(".")
Y=int(S[-1])
if Y<=2:
    print(S[:X]+"-")
elif Y<=6:
    print(S[:X])
else:
    print(S[:X]+"+")