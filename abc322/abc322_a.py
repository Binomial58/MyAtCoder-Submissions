N=int(input())
S=input()
if S.count("ABC")==0:
    print("-1")
else:
    print(S.index("ABC")+1)