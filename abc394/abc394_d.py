S=input()
L=[]
if len(S)%2==1:
    print("No")
    exit()
for i in range(len(S)):
    if S[i]=="(":
        L.append(1)
    elif S[i]=="[":
        L.append(2)
    elif S[i]=="<":
        L.append(3)
    if S[i]==")" or S[i]=="]" or S[i]==">":
        if len(L)==0:
            print("No")
            exit()
        elif L[-1]==1 and S[i]==")":
            del L[-1]
        elif L[-1]==2 and S[i]=="]":
            del L[-1]
        elif L[-1]==3 and S[i]==">":
            del L[-1]
        else:
            print("No")
            exit()
print("Yes")