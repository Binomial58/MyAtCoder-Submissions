S=input()
if int(S[2])==8:
    print(str(int(S[0])+1)+"-1")
else:
    print(S[:2]+str(int(S[2])+1))
