S=input()
T=input()
if T[-1]!="X":
    T=T.lower()
    if T[0] not in S or T[1] not in S[S.index(T[0])+1:] or T[2] not in S[S[S.index(T[0])+1:].index(T[1])+len(S)-len(S[S.index(T[0])+1:])+1:]:
        print("No")
    else:
        a=S.index(T[0])
        b=S[a+1:].index(T[1])+len(S)-len(S[a+1:])
        c=S[b+1:].index(T[2])+len(S)-len(S[b+1:])
        if a<b<c:
            print("Yes")
        else:
            print("No")
else:
    T=T[:2].lower()
    if T[0] not in S or T[1] not in S[S.index(T[0])+1:] :
        print("No")
    else:
        a=S.index(T[0])
        b=S[a+1:].index(T[1])+len(S)-len(S[a+1:])
        if a<b:
            print("Yes")
        else:
            print("No")
