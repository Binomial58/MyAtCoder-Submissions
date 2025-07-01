S=input()
R=set()
if len(S)%2==1:
    print("No")
else:
    for i in range(len(S)//2):
        if S[2*i]!=S[2*i+1] or S[2*i]in R:
            print("No")
            exit()
        R.add(S[2*i])
    print("Yes")
