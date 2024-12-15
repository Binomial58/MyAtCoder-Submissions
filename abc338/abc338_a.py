S=input()
L=len(S)
if L==1 and S.isupper():
    print("Yes")
else:
    if S[0].isupper() and (S[1:].islower()):
        print("Yes")
    else:
        print("No")