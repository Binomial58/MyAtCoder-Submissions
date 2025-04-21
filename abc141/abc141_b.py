S=input()
for i in range(1,len(S)+1):
    if i%2==1:
        if S[i-1]!="R" and S[i-1]!="U" and S[i-1]!="D":
            print("No")
            exit()
    else:
        if S[i-1]!="L" and S[i-1]!="U" and S[i-1]!="D":
            print("No")
            exit()
print("Yes")