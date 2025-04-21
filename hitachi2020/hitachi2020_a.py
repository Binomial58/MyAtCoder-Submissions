S=input()
if len(S)%2==1:
    print("No")
    exit()
else:
    for i in range(0,len(S),2):
        if S[i]!="h" or S[i+1]!="i":
            print("No")
            exit()
print("Yes")