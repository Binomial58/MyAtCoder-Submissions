S=input()
L=[int(S[6]),int(S[3]),int(S[7])+int(S[1]),int(S[4])+int(S[0]),int(S[8])+int(S[2]),int(S[5]),int(S[9])]
if S[0]=="1":
    print("No")
    exit()
else:
    for i in range(7):
        for j in range(7):
            if i<=j+1:
                break
            if L[i]>=1 and L[j]>=1:
                for k in range(j,i):
                    if L[k]==0:
                        print("Yes")
                        exit()
print("No")